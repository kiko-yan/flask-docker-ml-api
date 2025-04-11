# Exercise 2 Answers

---

## Question 1: ATE Estimation Using Linear Regression

### a) Estimated Parameters

Using linear regression on the observed data, I estimated the model:
The regression model used is:

**Y<sub>i</sub> = α + τ·W<sub>i</sub> + β·X<sub>i</sub> + ε<sub>i</sub>**


The estimated parameters are:

- **Intercept (α̂)**: `95.97`
- **Treatment Effect (τ̂)**: `-9.11`
- **Sustainability Spending Effect (β̂)**: `1.51`

---

### b) ATE and Statistical Significance

- The **Average Treatment Effect (τ̂)** is **-9.11**, suggesting that participation in the carbon offset program is associated with a **decrease** of ~9.11 points in engagement score, holding spending constant.
- Since the model was estimated using `scikit-learn`, statistical significance (p-values) are not provided. For hypothesis testing, a package like `statsmodels` would be used.

---

### c) Assumptions for Causal Interpretation

To interpret τ̂ causally, the following assumptions must be satisfied:

1. **Ignorability / Unconfoundedness**: Treatment assignment (W) is independent of potential outcomes, conditional on X.
2. **No omitted confounders**: All variables that affect both treatment and outcome are controlled.
3. **Correct model specification**: The linear regression form appropriately captures the data structure.
4. **SUTVA (Stable Unit Treatment Value Assumption)**: No interference between units.

---

## Question 2: Flask API and Containerization

### a) Codespaces & Docker Setup

- A GitHub Codespace environment was used.
- The environment is containerized via a `Dockerfile`, which installs Python, `Flask`, `NumPy`, and `scikit-learn`.
- Containerization ensures reproducibility and platform independence.

---

### b) Flask API

- The `app.py` script:
  - Trains a linear regression model using the dataset from Q1.
  - Provides a `/predict` endpoint that takes `w` (treatment) and `x` (spending) as input.
  - Returns predicted engagement score `Ŷ`, as well as model parameters.

---

### c) API Test Result

Tested using:

- `Wi = 1` (treated)
- `Xi = 20` ($20,000 spending)

Returned:

```json
{
  "w": 1.0,
  "x": 20.0,
  "predicted_engagement_score": 117.16,
  "intercept": 95.97,
  "treatment_effect (tau)": -9.11,
  "spending_effect (beta)": 1.51
}


