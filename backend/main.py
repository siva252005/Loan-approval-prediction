from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import numpy as np
import os
import sys

# Import xgboost to ensure it's available for pickle if needed
try:
    import xgboost
except ImportError:
    pass

app = FastAPI(title="Loan Approval Prediction API")

# Load model
# We look for model.pkl in the same directory as this script, or in the current working directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path_1 = os.path.join(current_dir, "model.pkl")
model_path_2 = "model.pkl"

model = None

# Try loading from possible locations
paths_to_try = [model_path_1, model_path_2]

for p in paths_to_try:
    if os.path.exists(p):
        try:
            with open(p, "rb") as f:
                model = pickle.load(f)
            print(f"Successfully loaded model from {p}")
            break
        except Exception as e:
            print(f"Failed to load model from {p}: {e}", file=sys.stderr)

if model is None:
    print("CRITICAL: Model file not found or could not be loaded.", file=sys.stderr)
    print(f"Searched in: {paths_to_try}", file=sys.stderr)
    print(f"CWD: {os.getcwd()}", file=sys.stderr)

class LoanApplication(BaseModel):
    Gender: str
    Married: str
    Dependents: str
    Education: str
    Self_Employed: str
    ApplicantIncome: float
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: float
    Property_Area: str

@app.get("/")
def read_root():
    return {"message": "Welcome to Loan Approval Prediction API"}

@app.post("/predict")
def predict(application: LoanApplication):
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")

    # Validation and Encoding
    gender_map = {'Male': 1, 'Female': 2}
    yes_no_map = {'Yes': 1, 'No': 2}
    education_map = {'Graduate': 1, 'Not Graduate': 2}
    property_map = {'Urban': 3, 'Semiurban': 2, 'Rural': 1}
    
    try:
        gender_val = gender_map.get(application.Gender)
        if gender_val is None: raise ValueError(f"Invalid Gender: {application.Gender}")

        married_val = yes_no_map.get(application.Married)
        if married_val is None: raise ValueError(f"Invalid Married status: {application.Married}")
        
        # Dependents handling
        dep = str(application.Dependents).replace(' ','')
        if dep == '3+':
            dep_val = 3
        else:
            try:
                dep_val = int(dep)
            except:
                raise ValueError(f"Invalid Dependents: {application.Dependents}")
            
        education_val = education_map.get(application.Education)
        if education_val is None: raise ValueError(f"Invalid Education: {application.Education}")

        self_employed_val = yes_no_map.get(application.Self_Employed)
        if self_employed_val is None: raise ValueError(f"Invalid Self_Employed: {application.Self_Employed}")
        
        property_val = property_map.get(application.Property_Area)
        if property_val is None: raise ValueError(f"Invalid Property_Area: {application.Property_Area}")
        
        features = [
            gender_val,
            married_val,
            dep_val,
            education_val,
            self_employed_val,
            application.ApplicantIncome,
            application.CoapplicantIncome,
            application.LoanAmount,
            application.Loan_Amount_Term,
            application.Credit_History,
            property_val
        ]
        
        # Features order check against notebook:
        # In notebook:
        # null_cols = ['Credit_History', 'Self_Employed', 'LoanAmount','Dependents', 'Loan_Amount_Term', 'Gender', 'Married']
        # The notebook drops Loan_ID.
        # The columns remaining (and their order) matters.
        # Based on typical notebook workflows, the order is usually the order of columns in the dataframe.
        # df.columns: Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area, Loan_Status
        # So the Feature Vector should probably be:
        # [Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area]
        
        # My previous code had Dependents at the end.
        
        # NOTE: I need to be careful about feature order.
        # In the notebook, `tr_df` had `Dependents` dropped and re-added at the end?
        # Notebook line 421: tr_df.drop(['Dependents'], axis = 1, inplace = True)
        # Notebook line 425: tr_df = pd.concat([tr_df, Dependents_], axis = 1)
        # YES! The notebook MOVED Dependents to the END of the dataframe.
        # So the order IS:
        # Gender, Married, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area, Dependents
        
        # My previous code:
        # features = [gender_val, married_val, education_val, self_employed_val, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, property_val, dep_val]
        # It matched the "Dependents at end" logic.
        
        # Let's verify the order in THIS updated file.
        # I constructed:
        # features = [gender_val, married_val, dep_val, education_val, ...]
        # Wait, in the code block ABOVE, I put `dep_val` at index 2 (3rd item).
        # This contradicts the notebook logic of "Dependents at the end".
        
        # ERROR IN THIS DRAFT: I just put `dep_val` earlier. I should fix this to match the notebook.
        
        final_features_list = [
            gender_val,
            married_val,
            education_val,
            self_employed_val,
            application.ApplicantIncome,
            application.CoapplicantIncome,
            application.LoanAmount,
            application.Loan_Amount_Term,
            application.Credit_History,
            property_val,
            dep_val
        ]
        
        final_features = np.array([final_features_list])
        prediction = model.predict(final_features)
        
        result = "Approved" if prediction[0] == 1 else "Rejected"
        
        return {"prediction": result, "status": int(prediction[0])}
        
    except Exception as e:
        print(f"Prediction Error: {e}", file=sys.stderr)
        raise HTTPException(status_code=500, detail=str(e))
