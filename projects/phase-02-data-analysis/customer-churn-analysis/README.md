# Project — Customer Churn Analysis (Portfolio)

**Phase:** Data Analysis  
**Skills:** Pandas, EDA, Seaborn, Statistical Analysis, Data Storytelling

---

## 📋 Project Overview

Analyse a telecom customer dataset to:
- Understand who churns and why
- Identify key churn drivers
- Build visualisations that tell the story
- Write actionable business recommendations

---

## 🎯 Business Context

Customer churn is one of the most costly problems for any subscription business.
Retaining an existing customer costs 5x less than acquiring a new one.

A typical analysis deliverable: "Customers with month-to-month contracts and electronic billing are 3x more likely to churn. Recommend offering a 10% discount for annual contract upgrades to this segment."

---

## 🗂️ Folder Structure

```text
customer-churn-analysis/
├── README.md
├── analysis.ipynb          ← main Jupyter notebook
├── data/
│   └── telecom_churn.csv   ← dataset (download link in notebook)
└── outputs/
    ├── churn_report.pdf
    └── charts/
```

---

## 📊 Analysis Steps

### 1. Data Understanding
- Load and inspect the dataset
- Check shape, dtypes, missing values
- Understand each column

### 2. Data Cleaning
- Handle missing values
- Fix data types (e.g., TotalCharges is string)
- Encode the target variable

### 3. Exploratory Data Analysis
- [ ] Churn rate overall (baseline)
- [ ] Churn by contract type
- [ ] Churn by payment method
- [ ] Churn by tenure (months)
- [ ] Churn by monthly charges
- [ ] Correlation heatmap

### 4. Statistical Analysis
- [ ] Chi-square test: contract type vs churn
- [ ] T-test: monthly charges — churned vs retained

### 5. Business Insights
- Write 5 actionable insights with supporting data
- Quantify the business impact

---

## 📁 Dataset

Download the Telco Customer Churn dataset from Kaggle:  
[https://www.kaggle.com/datasets/blastchar/telco-customer-churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

Place it in the `data/` folder.

---

## 💡 Hints

1. `df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')` to fix type
2. Use `df.groupby('Churn').agg(...)` for group comparisons
3. Use `sns.countplot()` for categorical features
4. Use `sns.boxplot()` to compare distributions
5. Use `df.corr()` + `sns.heatmap()` for correlations
