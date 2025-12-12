import streamlit as st
import requests
import json

st.set_page_config(page_title="Loan Approval Prediction", layout="wide", initial_sidebar_state="expanded")

# CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 20px;
        padding: 10px 24px;
        border-radius: 8px;
        width: 100%;
    }
    .success-msg {
        background-color: #d4edda;
        color: #155724;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        border: 2px solid #c3e6cb;
    }
    .error-msg {
        background-color: #f8d7da;
        color: #721c24;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        border: 2px solid #f5c6cb;
    }
    h1 {
        text-align: center; 
        color: #2c3e50;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🏦 Loan Approval Prediction System")
st.markdown("<p style='text-align: center; color: #555;'>End-to-end Machine Learning Solution</p>", unsafe_allow_html=True)
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("👤 Personal Details")
    gender = st.selectbox("Gender", ["Male", "Female"])
    married = st.selectbox("Marital Status", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Self Employed", ["Yes", "No"])

with col2:
    st.subheader("💰 Financial & Loan Details")
    applicant_income = st.number_input("Applicant Income ($)", min_value=0.0, value=5000.0, step=100.0)
    coapplicant_income = st.number_input("Coapplicant Income ($)", min_value=0.0, value=0.0, step=100.0)
    loan_amount = st.number_input("Loan Amount ($k)", min_value=0.0, value=120.0, step=1.0)
    loan_amount_term = st.selectbox("Loan Amount Term (Months)", [360.0, 180.0, 480.0, 300.0, 240.0, 120.0, 60.0, 84.0, 12.0])
    credit_history = st.selectbox("Credit History", [1.0, 0.0], format_func=lambda x: "Good (1.0)" if x == 1.0 else "Bad (0.0)")
    property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

st.markdown("###")
predict_btn = st.button("Predict Loan Status")

if predict_btn:
    
    with st.spinner("Analyzing your application..."):
        # Prepare payload
        payload = {
            "Gender": gender,
            "Married": married,
            "Dependents": dependents,
            "Education": education,
            "Self_Employed": self_employed,
            "ApplicantIncome": applicant_income,
            "CoapplicantIncome": coapplicant_income,
            "LoanAmount": loan_amount,
            "Loan_Amount_Term": loan_amount_term,
            "Credit_History": credit_history,
            "Property_Area": property_area
        }
        
        try:
            # Assumes backend is running on localhost:8000
            response = requests.post("http://127.0.0.1:8000/predict", json=payload)
            
            if response.status_code == 200:
                result = response.json()
                status = result["prediction"]
                
                st.markdown("---")
                if status == "Approved":
                    st.balloons()
                    st.markdown(f'<div class="success-msg">🎉 Congratulations! Your loan is APPROVED.</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="error-msg">⚠️ Sorry, your loan is REJECTED.</div>', unsafe_allow_html=True)
            else:
                st.error(f"Error from server: {response.text}")
                
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to the backend server. Please ensure the API is running.")
            st.info("To run the backend: `uvicorn backend.main:app --reload`")

st.markdown("---")
st.markdown("<div style='text-align: center'>Built with ❤️ using Streamlit & FastAPI</div>", unsafe_allow_html=True)
