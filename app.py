#import libraries
import re
import numpy as np # type: ignore
from flask import Flask, request, jsonify, render_template, redirect
import pickle
import math as math

app = Flask(__name__)

# Load the models
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def hello():
    return render_template("index.html")

@app.route('/aboutUs', methods=['GET'])
def aboutUs():
    return render_template('aboutUs.html')

@app.route('/api', methods=['POST'])
def predict():
    # Extract form data
    try:
        name = request.form['name']
        email = request.form['email']
        
       
        age = float(request.form['age'])
        gender = int(request.form['gender'])
        blood_pressure = float(request.form['blood_pressure'])
        cholesterol = float(request.form['cholesterol'])
        # Add other features as necessary

        # Prepare the feature array for prediction
        features = np.array([[age, gender, blood_pressure, cholesterol]])
        
        # Predict using the model
        prediction = model.predict(features)
        
        # Assuming the model outputs 0 or 1 for heart disease
        result = 'Heart Disease Detected' if prediction[0] == 1 else 'No Heart Disease Detected'

        return render_template('result.html', name=name, email=email, result=result)
    
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
