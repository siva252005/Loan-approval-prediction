import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import os
import urllib.request

# 1. Download Data
train_url = "https://raw.githubusercontent.com/Architectshwet/Loan-prediction-using-Machine-Learning-and-Python/master/data/train_u6lujuX_CVtuZ9i.csv"
train_path = "train.csv"

if not os.path.exists(train_path):
    print("Downloading train.csv...")
    urllib.request.urlretrieve(train_url, train_path)

# 2. Load and Preprocess
df = pd.read_csv(train_path)

# Drop ID
if 'Loan_ID' in df.columns:
    df.drop('Loan_ID', axis=1, inplace=True)

# Fill Missing Values
null_cols = ['Credit_History', 'Self_Employed', 'LoanAmount','Dependents', 'Loan_Amount_Term', 'Gender', 'Married']
for col in null_cols:
    df[col] = df[col].fillna(df[col].dropna().mode().values[0])

# Encoding
to_numeric = {
    'Male': 1, 'Female': 2,
    'Yes': 1, 'No': 2,
    'Graduate': 1, 'Not Graduate': 2,
    'Urban': 3, 'Semiurban': 2, 'Rural': 1,
    'Y': 1, 'N': 0,
    '3+': 3
}

df = df.applymap(lambda label: to_numeric.get(label) if label in to_numeric else label)

# Handle Dependents
# Notebook logic: drop 'Dependents', convert to numeric, add back at end.
# Note: '3+' was mapped to 3 in the map above.
# Use pd.to_numeric to catch any strings that didn't get mapped (like '0', '1', '2' which are strings in CSV?)
# The CSV usually has strings '0', '1', '2', '3+'.
# My map handles '3+'. The others '0','1','2' need conversion.

# Check unique values in Dependents
# In notebook: Dependents_ = pd.to_numeric(tr_df.Dependents)
# This works if '0','1','2' are present. '3+' became 3 (int) in previous step?
# Wait, `applymap` applies to all elements.
# If Dependents has '0' (str), `to_numeric.get('0')` is None, so it returns '0'.
# Then `pd.to_numeric` converts '0' to 0 (int).

# Replicating notebook exact steps for Dependents
dep_numeric = pd.to_numeric(df.Dependents)
df.drop(['Dependents'], axis=1, inplace=True)
df = pd.concat([df, dep_numeric], axis=1)

# Split X and y
y = df['Loan_Status']
X = df.drop('Loan_Status', axis=1)

print("Feature columns order:", X.columns.tolist())
# Expected: Gender, Married, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area, Dependents

# 3. Train Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {acc*100:.2f}%")

# 4. Save Model
output_path = "model.pkl"
with open(output_path, "wb") as f:
    pickle.dump(model, f)

print(f"Model saved to {output_path}")

# Also copy to backend
import shutil
if not os.path.exists("backend"):
    os.makedirs("backend")
shutil.copy(output_path, "backend/model.pkl")
print("Model copied to backend/model.pkl")
