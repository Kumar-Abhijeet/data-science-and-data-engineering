# Machine Learning Quick Reference

## Algorithm Selection Guide

| Problem | Data | Algorithm |
|---------|------|-----------|
| Predict a number | Labeled | Linear Regression, Random Forest Regressor, XGBoost |
| Classify into categories | Labeled | Logistic Regression, Random Forest, XGBoost, SVM |
| Find groups | Unlabeled | K-Means, DBSCAN, Hierarchical |
| Reduce dimensions | Any | PCA, t-SNE, UMAP |
| Detect anomalies | Unlabeled | Isolation Forest, One-Class SVM |

---

## Model Evaluation Metrics

### Regression
| Metric | Formula | Notes |
|--------|---------|-------|
| MAE | mean(|y - ŷ|) | Easy to interpret, same unit as target |
| RMSE | √mean((y-ŷ)²) | Penalises large errors more |
| R² | 1 - SS_res/SS_tot | % variance explained (1.0 = perfect) |
| MAPE | mean(|y-ŷ|/y) × 100 | % error, scale-independent |

### Classification
| Metric | Use When |
|--------|---------|
| Accuracy | Balanced classes |
| Precision | Cost of false positive is high (spam filter) |
| Recall | Cost of false negative is high (fraud, cancer detection) |
| F1 Score | Imbalanced classes |
| ROC-AUC | Ranking quality, threshold-independent |

---

## Confusion Matrix

```
                  Predicted
                  Pos    Neg
Actual  Pos   [ TP  |  FN ]
        Neg   [ FP  |  TN ]

Precision = TP / (TP + FP)   → of all positives predicted, how many are correct?
Recall    = TP / (TP + FN)   → of all actual positives, how many did we catch?
F1        = 2 * P * R / (P + R)
```

---

## sklearn Pipeline Pattern

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier

numeric_features = ['age', 'income', 'score']
categorical_features = ['city', 'status']

preprocessor = ColumnTransformer([
    ('num', StandardScaler(), numeric_features),
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
])

pipeline = Pipeline([
    ('prep', preprocessor),
    ('model', RandomForestClassifier(n_estimators=100, random_state=42))
])

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
```

---

## Overfitting vs Underfitting

| | Train Score | Test Score | Fix |
|---|-------------|------------|-----|
| Underfitting | Low | Low | More features, complex model |
| Good fit | High | High | ✓ |
| Overfitting | Very high | Low | Regularisation, more data, simpler model |

---

## Hyperparameter Tuning

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'model__n_estimators': [100, 200, 300],
    'model__max_depth': [3, 5, 10, None],
    'model__min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='roc_auc', n_jobs=-1)
grid_search.fit(X_train, y_train)
print(f"Best params: {grid_search.best_params_}")
print(f"Best score : {grid_search.best_score_:.4f}")
```
