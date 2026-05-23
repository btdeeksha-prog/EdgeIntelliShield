import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

# Page Config
st.set_page_config(page_title="Edge IntelliShield", page_icon="🛡️", layout="wide")

# Custom UI Styling
st.markdown("""
    <style>
    .main { background-color: #0f172a; color: #f8fafc; }
    .stButton>button { width: 100%; background-color: #06b6d4; color: white; border: none; padding: 12px; border-radius: 8px; font-weight: bold; font-size: 16px; }
    .fraud-box { background-color: #7f1d1d; padding: 25px; border-radius: 12px; border: 1px solid #f87171; text-align: center; }
    .safe-box { background-color: #064e3b; padding: 25px; border-radius: 12px; border: 1px solid #34d399; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Edge IntelliShield")
st.markdown("### Real-Time ML Fraud Detection Dashboard")
st.write("Enter transaction details below to check if it's Safe or Fraudulent.")

# Load Model
@st.cache_resource
def load_model():
    model_path = os.path.join('models', 'fraud_model.pkl')
    if os.path.exists(model_path):
        with open(model_path, 'rb') as f:
            return pickle.load(f)
    return None

model = load_model()

# Inputs Layout
col1, col2 = st.columns(2)
with col1:
    st.subheader("Transaction Info")
    trans_type = st.selectbox("Transaction Type", ["TRANSFER", "CASH_OUT", "PAYMENT", "CASH_IN", "DEBIT"])
    amount = st.number_input("Transaction Amount ($)", min_value=0.0, value=100.0)

with col2:
    st.subheader("Account Metrics")
    old_balance = st.number_input("Sender's Old Balance", min_value=0.0, value=500.0)
    new_balance = st.number_input("Sender's New Balance", min_value=0.0, value=400.0)

type_map = {"TRANSFER": 1, "CASH_OUT": 2, "PAYMENT": 3, "CASH_IN": 4, "DEBIT": 5}
type_encoded = type_map[trans_type]

if st.button("🚀 ANALYZE TRANSACTION"):
    if model is not None:
        try:
            input_features = np.array([[type_encoded, amount, old_balance, new_balance]])
            prediction = model.predict(input_features)
            
            st.markdown("---")
            if prediction[0] == 1:
                st.markdown('<div class="fraud-box"><h2 style="color:white; margin:0;">⚠️ FRAUDULENT TRANSACTION</h2><p style="color:#fecaca; margin:5px 0 0 0;">The model flagged this transaction as highly suspicious!</p></div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="safe-box"><h2 style="color:white; margin:0;">✅ LEGITIMATE TRANSACTION</h2><p style="color:#d1fae5; margin:5px 0 0 0;">Transaction pattern is safe and normal.</p></div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Prediction Error: {e}")
    else:
        # Demo Mode (Agar model file load na ho paye)
        st.warning("⚠️ Note: Running in Demo Mode (Actual 'fraud_model.pkl' not detected inside 'models/' folder).")
        if amount > 50000 and trans_type in ["TRANSFER", "CASH_OUT"]:
            st.markdown('<div class="fraud-box"><h2 style="color:white; margin:0;">⚠️ FRAUD ALERT (Demo Mode)</h2></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="safe-box"><h2 style="color:white; margin:0;">✅ LEGITIMATE (Demo Mode)</h2></div>', unsafe_allow_html=True)