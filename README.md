# Project Overview

This project implements a linear regression model to estimate the causal effect of a carbon offset program on corporate stakeholder engagement scores, following the Rubin Causal Model. The model is containerized using Docker and exposed via a Flask API for easy deployment and prediction.

---

## Components

- **`app.py`**  
  Trains a linear regression model using the provided dataset and exposes a `/predict` endpoint via Flask.  
  The endpoint accepts:
  - `w` → binary treatment indicator (0 or 1)
  - `x` → sustainability spending ($1,000s)  
  and returns:
  - predicted engagement score
  - regression coefficients

- **`Dockerfile`**  
  Builds a Docker image that installs Python, `flask`, `numpy`, and `scikit-learn`, and runs the Flask app.  
  By containerizing the setup, it ensures the application runs consistently across different machines and platforms, improving reproducibility and easing deployment.
  
- **`requirements.txt`**  
  Lists required Python packages (`flask`, `scikit-learn`, `numpy`) for reproducibility.

---

## Running the App with Docker

### 🛠 Build the Docker Image
`docker build -t my-causal-app .`

### **🚀 Run the Container**
`docker run -p 5002:5000 my-causal-app`

### **🔍 Test the API**
`curl "http://localhost:5002/predict?w=1&x=20"`
