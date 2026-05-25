# Project — House Price Prediction

**Phase:** Machine Learning  
**Skills:** Linear Regression, Feature Engineering, EDA, sklearn Pipeline

---

## 📋 Project Overview

Build a regression model to predict house prices based on property features.

---

## 🎯 Business Context

Real estate portals (Magicbricks, 99acres) use ML models to display estimated prices.
Mortgage companies use them for property valuation.

---

## ⚙️ Steps to Build

- [ ] EDA: distribution of prices, correlation with features
- [ ] Feature engineering: area per room, age of property
- [ ] Baseline: Linear Regression
- [ ] Advanced: Random Forest / XGBoost
- [ ] Evaluation: RMSE, MAE, R²
- [ ] Visualise: actual vs predicted scatter plot

---

## 📁 Dataset

Use the Bangalore house price dataset from Kaggle, or the Boston/California housing dataset from sklearn:

```python
from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing(as_frame=True)
df = housing.frame
```

---

## 💡 Key Learning Points

- Handling skewed target variable (log transformation)
- Outlier removal (price per sqft)
- Encoding location (high-cardinality categorical)
- Regularisation: Ridge vs Lasso vs ElasticNet
