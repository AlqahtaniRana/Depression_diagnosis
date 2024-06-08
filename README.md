# Early Diagnosis of Depression Using Machine Learning

## Description
This project aims to predict whether an individual is suffering from depression using a dataset from Zindi. The dataset includes survey responses related to mental health in East Africa. We employ machine learning models to achieve this goal and provide a user-friendly web interface to input data and get predictions.

## Project Structure
- `app.py`: Flask application to serve the web interface and handle predictions.
- `templates/`: Contains the HTML template (`index.html`) for the web interface.
- `model.pkl`: The trained machine learning model serialized using joblib.
- `README.md`: Project documentation.
- `Early Diagnosis of Depression.pdf`: Contains the Capstone Project documentation.


## Dependencies
- Python 3.7+
- Flask
- joblib
- numpy
- scikit-learn
- pandas
- imbalanced-learn
- matplotlib
- seaborn

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/AlqahtaniRana/Depression_diagnosis.git
    cd Depression_diagnosis
    ```
2. Create a virtual environment and activate it:
    ```bash
    python -m venv env
    source env/bin/activate   # On Windows: `.\env\Scripts\activate`
    ```
3. Install the required libraries:
    ```bash
    pip install Flask joblib numpy scikit-learn pandas imbalanced-learn
    ```

## Usage
1. **Run the Flask Application**:
    ```bash
    python app.py
    ```
2. **Access the Web Interface**:
    - Navigate to `http://127.0.0.1:5000/` in your web browser.
    - Fill in the form with the required features and submit to get the prediction at the end of the page.

## License
This project was completed as part of the Udacity Data Scientist Nanodegree program.

## Additional Documentation
The file `Early Diagnosis of Depression.pdf` contains the detailed Capstone Project documentation, providing a comprehensive overview of the project's objectives, methodology, results, and conclusions.
