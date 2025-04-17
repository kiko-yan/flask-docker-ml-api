
## Question 1

### a) Estimated Parameters

**Model**: Y<sub>i</sub> = α + τ·W<sub>i</sub> + β·X<sub>i</sub> + ε<sub>i</sub>

- Intercept (α̂): `95.97`
- Treatment Effect (τ̂): `-9.11`
- Spending Effect (β̂): `1.51`

---

### b) Estimated ATE

- τ̂ = `-9.11`
- No p-values available (used `scikit-learn`)

---

### c) Causal Assumptions

- Treatment is unconfounded
- No omitted variables
- Linear model is correct
- SUTVA holds

---

## Question 2

### a) Setup

- Environment: GitHub Codespaces + Dockerfile
- Tools: Python, Flask, NumPy, scikit-learn

---

### b) API

- Endpoint: `/predict?w=1&x=20`
- Returns predicted score and model parameters

---

### c) Test Result

Input:
- w = 1
- x = 20

Output:

```json
{
  "w": 1.0,
  "x": 20.0,
  "predicted_engagement_score": 117.16,
  "intercept": 95.97,
  "treatment_effect (tau)": -9.11,
  "spending_effect (beta)": 1.51
}



