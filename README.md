# 🏦 Bank Loan Approval Prediction 💳📊

This project predicts whether a loan application will be approved or rejected based on applicant details.  

Using **Python, Machine Learning, FastAPI, and Streamlit**, it builds a complete ML pipeline from data preprocessing to deployment.

**Workflow:**  
Data Collection → Data Cleaning → Feature Engineering → Model Training → API Development → Streamlit UI  

---

## 📊 Project Status
✅ Project Completed  

---

## 🚀 How to Run this Project

### 1. Setup Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
.venv\Scripts\activate           # Windows
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
*(Dependencies include FastAPI, scikit-learn, Pandas, NumPy, Streamlit, XGBoost, etc.)*

### 3. Train the Model
```bash
python train_model.py
```

### 4. Run the Backend API
```bash
uvicorn backend.main:app --reload
```

### 5. Run the Frontend (Streamlit UI)
```bash
streamlit run frontend/app.py
```

---

## 📊 Application Preview

### Loan Prediction Web App

- Input applicant details  
- Predict loan approval (Approved / Rejected)  
- Real-time prediction using the trained ML model  

---

## 📈 Key Insights

- **Credit History** is the most important factor for loan approval  
- **Higher Applicant Income** increases approval chances  
- **Loan Amount** and **Loan Term** influence approval probability  
- Married applicants have slightly higher approval rates  
- Applicants in economies/urban areas tend to get more approvals  

---

## 🛠 Skills Demonstrated

- Data cleaning using Python (Pandas)  
- Feature engineering  
- Machine Learning model building (Logistic Regression)  
- Model evaluation (Accuracy Score)  
- API development using FastAPI  
- Frontend development using Streamlit  
- Model deployment (End-to-end ML pipeline)  

---

## 🏗️ Project Structure
```text
PROJECT/
│
├── .venv/ # Virtual environment
│
├── backend/
│   ├── __pycache__/ # Auto-generated cache
│   ├── main.py # FastAPI backend
│   └── model.pkl # Saved trained model
│
├── frontend/
│   └── app.py # Streamlit UI
│
├── venv/ # Optional additional venv
│
├── .gitignore
├── check_header.py
├── how to run.txt
├── inspect_model.py
├── loan-prediction-dataset-ml-project.ipynb
├── model.pkl # Saved model (backup/copy)
├── README.md
├── requirements.txt
├── test.txt
├── train_model.py
├── train.csv # Dataset
└── try_load.py
```

---

## 🚀 Implementation Phases

### 🟩 Phase 1 – Dataset Collection
- **Objective:** Understand dataset structure  
- Dataset obtained from an online source  
- Analyzed features like income, credit history, loan amount  
- Identified missing values  
- **Status:** ✅ Completed  

---

### 🟨 Phase 2 – Data Cleaning & Preprocessing
- **Objective:** Prepare dataset for the ML model  
- Handled missing values using mode  
- Removed unnecessary columns (e.g., `Loan_ID`)  
- Converted categorical data into numerical format  
- **Status:** ✅ Completed  

---

### 🟦 Phase 3 – Feature Engineering
- **Objective:** Improve model performance  
- Encoded categorical variables  
- Converted `Dependents` column to numeric  
- Selected important features  
- **Status:** ✅ Completed  

---

### 🟧 Phase 4 – Model Training & Evaluation
- **Objective:** Train ML model  
- Algorithm used: **Logistic Regression**  
- Split dataset into training & testing sets  
- Evaluated using accuracy score  
- **Status:** ✅ Completed  

---

### 🟥 Phase 5 – Deployment
- **Objective:** Build a real-time prediction system  
- Backend API using **FastAPI**  
- Frontend UI using **Streamlit**  
- Model integration using **Pickle (.pkl file)**  
- Real-time predictions  
- **Status:** ✅ Completed  

---

## 🛠 Technical Stack

| Category           | Tools |
|--------------------|-----------------------------------------|
| Data Processing    | Python, Pandas, NumPy                  |
| ML Model           | Scikit-learn (Logistic Regression)     |
| Backend            | FastAPI, Uvicorn                       |
| Frontend           | Streamlit                                |
| Deployment         | Pickle Model                           |
| Version Control    | Git, GitHub                            |

---

## 🎯 Workflow Pipeline
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

text

---

## 💼 Interview Talking Point

“I built an end‑to‑end machine learning system for **bank loan approval prediction**, including data preprocessing, feature engineering, and training a **Logistic Regression model**. The model is deployed using **FastAPI** and integrated with an interactive **Streamlit UI** for real‑time predictions.”

---

## 🏁 Conclusion

This project demonstrates a complete ML lifecycle, from data processing and model building to deployment into a real‑world application. It highlights the importance of **data quality, feature engineering, and model interpretability** in decision‑critical domains like banking.