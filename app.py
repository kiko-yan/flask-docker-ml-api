from flask import Flask, request, jsonify
from sklearn.linear_model import LinearRegression
import numpy as np

app = Flask(__name__)

# Training data (W = treatment, X = sustainability spending)
W = np.array([0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1])
X = np.array([19.8, 23.4, 27.7, 24.6, 21.5, 25.1, 22.4, 29.3, 20.8, 20.2,
              27.3, 24.5, 22.9, 18.4, 24.2, 21.0, 25.9, 23.2, 21.6, 22.8])
Y = np.array([137, 118, 124, 124, 120, 129, 122, 142, 128, 114,
              132, 130, 130, 112, 132, 117, 134, 132, 121, 128])

# Stack W and X into a 2D feature array
features = np.column_stack((W, X))
model = LinearRegression().fit(features, Y)
print("Intercept (α):", model.intercept_)
print("Coefficients (τ, β):", model.coef_)

@app.route("/predict")
def predict():
    w = float(request.args.get("w", 0))
    x = float(request.args.get("x", 0))
    prediction = model.predict([[w, x]])[0]

    return jsonify({
        "w": w,
        "x": x,
        "predicted_engagement_score": prediction,
        "intercept": model.intercept_,
        "treatment_effect (tau)": model.coef_[0],
        "spending_effect (beta)": model.coef_[1]
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
