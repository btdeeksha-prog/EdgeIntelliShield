# Edge IntelliShield

A Machine Learning based Fraud Detection Project built to identify and analyze suspicious transactions using Python, Pandas, and Scikit-Learn.

## Project Structure
- data/: Contains transactions.csv (Dataset used for training and testing).
- models/: Contains the trained fraud_model.pkl file.
- notebooks/: Contains fraud_model.ipynb (The main Jupyter Notebook with code, analysis, and model training).

## How to Setup and Run

### 1. Clone the Repository
```bash
git clone [https://github.com/btdeeksha-prog/EdgeIntelliShield.git](https://github.com/btdeeksha-prog/EdgeIntelliShield.git)
cd EdgeIntelliShield
# 🛡️ Edge IntelliShield - Real-Time ML Fraud Detection

This is a Machine Learning-based Fraud Detection Project built to identify and analyze suspicious financial transactions using Python, Streamlit, and Scikit-Learn.

---

## 🚀 How to Run the Project Locally

Follow these simple steps to install and run the interactive dashboard on your local system:

### 1. Download the Project
Click on the green *Code* button at the top of this GitHub page, select *Download ZIP*, and extract the files on your computer.

### 2. Install Required Dependencies
Open your Command Prompt (cmd) or Terminal inside the extracted project folder and run the following command to install the required libraries:
```bash
pip install streamlit pandas numpy scikit-learn
python -m streamlit run (app.py)
---

## 📊 How to Test the Model (Input & Output)

As soon as you run the command, a local web page will automatically open in your browser (usually at http://localhost:8501). You can test the dynamic machine learning predictions using the following fields:

* *Transaction Info (Left Column):* Select the *Transaction Type* (e.g., TRANSFER, CASH_OUT, PAYMENT) and enter the *Transaction Amount ($)*.
* *Account Metrics (Right Column):* Input the sender's account balances (*Sender's Old Balance* and *Sender's New Balance*).
* *Get Results:* Click on the blue *ANALYZE TRANSACTION* button. The background machine learning model will immediately evaluate the features and display an interactive card:
  * *✅ LEGITIMATE TRANSACTION* (Green Box) for normal transaction behaviors.
  * *⚠️ FRAUDULENT TRANSACTION* (Red Box) for highly suspicious patterns.
