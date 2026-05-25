# Project — Lead Conversion Prediction (Portfolio)

**Phase:** Machine Learning  
**Skills:** Logistic Regression, Random Forest, Feature Engineering, Model Evaluation, sklearn Pipeline

---

## 📋 Project Overview

Build a machine learning model that predicts whether a sales lead will convert to a customer, using historical CRM data.

---

## 🎯 Business Context

Sales teams have thousands of leads but limited time. A conversion prediction model helps prioritise which leads to focus on — maximising revenue while reducing wasted effort.

This is a core ML application in any B2B or B2C sales-driven company.

---

## 🗂️ Folder Structure

```text
lead-conversion-prediction/
├── README.md
├── 01_eda.ipynb                ← exploration and visualisations
├── 02_feature_engineering.ipynb
├── 03_model_training.ipynb
├── 04_evaluation.ipynb
├── model.py                   ← final pipeline code
├── data/
│   └── leads.csv
└── models/
    └── lead_conversion_pipeline.pkl
```

---

## 📊 Features (Input Variables)

| Feature | Type | Description |
|---------|------|-------------|
| age | numeric | Lead's age |
| annual_income | numeric | Lead's annual income |
| lead_score | numeric | CRM-assigned lead score |
| source | categorical | Lead source (Website/Referral/Event) |
| city | categorical | City |
| total_visits | numeric | Website visits |
| time_on_site | numeric | Total minutes on site |
| is_contacted | binary | Whether the lead was called |

**Target:** `converted` (1 = Yes, 0 = No)

---

## ⚙️ Steps to Build

### Step 1 — EDA
- [ ] Class balance check (conversion rate)
- [ ] Feature distributions
- [ ] Correlation with target

### Step 2 — Feature Engineering
- [ ] Encode categorical features (OneHotEncoder)
- [ ] Scale numerical features (StandardScaler)
- [ ] Handle missing values
- [ ] Create ColumnTransformer

### Step 3 — Model Training
- [ ] Logistic Regression (baseline)
- [ ] Random Forest
- [ ] XGBoost
- [ ] Cross-validation (5-fold)

### Step 4 — Evaluation
- [ ] Confusion matrix
- [ ] Classification report (precision, recall, F1)
- [ ] ROC-AUC curve
- [ ] Feature importance plot

### Step 5 — Pipeline & Deployment
- [ ] Wrap preprocessing + model in sklearn Pipeline
- [ ] Save with joblib
- [ ] Write a `predict(lead_data)` function

---

## 💡 Business Interpretation

After building the model:
- Identify the top 3 factors that predict conversion
- Recommend which lead segments to prioritise
- Calculate estimated revenue impact of using the model vs random outreach
