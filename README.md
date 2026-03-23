🏦 Bank Loan Approval Prediction 💳📊

This project predicts whether a loan application will be approved or rejected based on applicant details.

Using Python, Machine Learning, FastAPI, and Streamlit, the project builds a complete ML pipeline from data preprocessing to deployment.

Data Collection → Data Cleaning → Feature Engineering → Model Training → API Development → Streamlit UI

---

📊 Project Status
✅ Project Completed

---

🚀 How to Run this Project

### 1. Setup Virtual Environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

### 2. Install Dependencies
pip install -r requirements.txt

(Dependencies include FastAPI, scikit-learn, pandas, numpy, streamlit, xgboost, etc.) :contentReference[oaicite:0]{index=0}

### 3. Train Model
python train_model.py

### 4. Run Backend API
uvicorn backend.main:app --reload

### 5. Run Frontend (Streamlit UI)
streamlit run frontend/app.py

(Alternative commands available) :contentReference[oaicite:1]{index=1}

---

📊 Application Preview

Loan Prediction Web App

- Input applicant details
- Predict loan approval (Approved / Rejected)
- Real-time prediction using trained ML model

---

📈 Key Insights

- Credit History is the most important factor for loan approval
- Higher Applicant Income increases approval chances
- Loan Amount and Loan Term influence approval probability
- Married applicants have slightly higher approval rates
- Applicants in urban areas tend to get more approvals

---

🛠 Skills Demonstrated

- Data Cleaning using Python (Pandas)
- Feature Engineering
- Machine Learning Model Building (Logistic Regression)
- Model Evaluation (Accuracy Score)
- API Development using FastAPI
- Frontend Development using Streamlit
- Model Deployment (End-to-End ML Pipeline)

---

🏗️ Project Structure

PROJECT/
│
├── .venv/
│
├── backend/
│   ├── __pycache__/
│   ├── main.py
│   └── model.pkl
│
├── frontend/
│   └── app.py
│
├── venv/
│
├── .gitignore
├── check_header.py
├── how to run.txt
├── inspect_model.py
├── loan-prediction-dataset-ml-project.ipynb
├── model.pkl
├── README.md
├── requirements.txt
├── test.txt
├── train_model.py
├── train.csv
└── try_load.py

---

🚀 Implementation Phases

🟩 Phase 1 – Dataset Collection  
Objective: Understand dataset structure.

- Dataset obtained from online source
- Analyzed features like income, credit history, loan amount
- Identified missing values  
Status: ✅ Completed

---

🟨 Phase 2 – Data Cleaning & Preprocessing  
Objective: Prepare dataset for ML model.

- Handled missing values using mode
- Removed unnecessary columns (Loan_ID)
- Converted categorical data into numerical format  
Status: ✅ Completed

---

🟦 Phase 3 – Feature Engineering  
Objective: Improve model performance.

- Encoded categorical variables
- Converted Dependents column to numeric
- Selected important features  
Status: ✅ Completed

---

🟧 Phase 4 – Model Training & Evaluation  
Objective: Train ML model.

- Algorithm used: Logistic Regression
- Split dataset into training & testing
- Evaluated using accuracy score (~model output)  
Status: ✅ Completed

---

🟥 Phase 5 – Deployment  
Objective: Build real-time prediction system.

- Backend API using FastAPI
- Frontend UI using Streamlit
- Model integration using pickle (.pkl file)
- Real-time predictions  
Status: ✅ Completed

---

🛠 Technical Stack

Category        Tools
-----------------------------------
Data Processing Python, Pandas, NumPy
ML Model        Scikit-learn (Logistic Regression)
Backend         FastAPI, Uvicorn
Frontend        Streamlit
Deployment      Pickle Model
Version Control Git, GitHub

---

🎯 Workflow Pipeline

Loan Dataset (CSV)
        ↓
Data Cleaning (Python / Pandas)
        ↓
Feature Engineering
        ↓
Model Training (Logistic Regression)
        ↓
Model Saved (model.pkl)
        ↓
FastAPI Backend
        ↓
Streamlit Frontend
        ↓
Loan Approval Prediction

---

💼 Interview Talking Point

Built an end-to-end machine learning system for bank loan approval prediction. Performed data preprocessing, feature engineering, and trained a Logistic Regression model. Deployed the model using FastAPI and created an interactive Streamlit interface for real-time predictions.

---

🏁 Conclusion

This project demonstrates a complete ML lifecycle including data processing, model building, and deployment into a real-world application.
