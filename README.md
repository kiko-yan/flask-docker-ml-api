Project Overview
This project implements a linear regression model to estimate the causal effect of a carbon offset program on corporate stakeholder engagement scores, following the Rubin Causal Model. The model is containerized using Docker and exposed via a Flask API for easy deployment and prediction.

Components
app.py: This script trains a linear regression model using the provided dataset and exposes a /predict endpoint via Flask. The endpoint accepts treatment status (W) and sustainability spending (X) as inputs and returns the predicted engagement score (Y).

Dockerfile: Configures a Docker container with Python 3.10, installs dependencies from requirements.txt, and runs the Flask app. Containerization ensures the application runs consistently across different environments, enhancing reproducibility.

requirements.txt: Lists the Python dependencies (flask, scikit-learn, numpy) required for the project, ensuring all users can install the correct versions effortlessly.
