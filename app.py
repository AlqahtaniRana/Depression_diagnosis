from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

# Initialize the Flask application
app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')  # Replace 'model.pkl' with the path to your saved model

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the POST request
    data = request.form.to_dict()
    data_values = [float(data[key]) for key in data.keys()]
    
    # Convert data into numpy array and reshape for prediction
    features = np.array(data_values).reshape(1, -1)
    
    # Make prediction
    prediction = model.predict(features)
    
    # Return the result
    result = 'Depressed' if prediction[0] == 1 else 'Not Depressed'
    return render_template('index.html', prediction_text='Prediction: {}'.format(result))

if __name__ == "__main__":
    app.run(debug=True)
