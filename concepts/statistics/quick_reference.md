# Statistics Quick Reference

## Descriptive Statistics

| Measure | Formula | When to Use |
|---------|---------|-------------|
| Mean | sum / count | Symmetric data, no extreme outliers |
| Median | middle value | Skewed data, outliers present (salaries, house prices) |
| Mode | most frequent | Categorical data |
| Std Dev | √variance | Spread around the mean |
| IQR | Q3 - Q1 | Robust measure of spread, outlier detection |

---

## Distributions

### Normal Distribution
- Bell-shaped, symmetric
- 68% of data within ±1 std dev
- 95% within ±2 std dev
- 99.7% within ±3 std dev
- Examples: heights, test scores, measurement errors

### Skewed Distributions
- **Right-skewed (positive):** mean > median — incomes, house prices
- **Left-skewed (negative):** mean < median — age at retirement

---

## Hypothesis Testing Framework

```
1. State H₀ (null) and H₁ (alternative)
2. Choose significance level α (typically 0.05)
3. Run the test → get p-value
4. If p < α: reject H₀ (statistically significant)
5. If p ≥ α: fail to reject H₀
```

### Common Tests
| Test | When to Use | Python |
|------|-------------|--------|
| t-test (one-sample) | Compare sample mean to known value | `scipy.stats.ttest_1samp` |
| t-test (two-sample) | Compare two group means | `scipy.stats.ttest_ind` |
| Chi-square | Independence of categorical variables | `scipy.stats.chi2_contingency` |
| ANOVA | Compare 3+ group means | `scipy.stats.f_oneway` |

---

## Correlation

```python
import pandas as pd
# Pearson correlation (linear, continuous data)
df.corr()

# Spearman correlation (ordinal, non-linear)
df.corr(method='spearman')
```

| r value | Interpretation |
|---------|----------------|
| 0.9–1.0 | Very strong positive |
| 0.7–0.9 | Strong positive |
| 0.4–0.7 | Moderate positive |
| 0.1–0.4 | Weak positive |
| 0.0 | No correlation |
| Negative | Inverse relationship |

---

## Linear Regression

```
y = β₀ + β₁x₁ + β₂x₂ + ... + ε

β₀ = intercept (value when all x = 0)
βᵢ = coefficient (change in y for unit change in xᵢ)
R² = proportion of variance explained (0–1, higher is better)
RMSE = average prediction error in original units
```

### Key Assumptions
1. Linearity — relationship between X and y is linear
2. Independence — observations are independent
3. Homoscedasticity — constant variance of residuals
4. Normality — residuals are normally distributed
