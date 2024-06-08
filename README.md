# Early Diagnosis of Depression Using Machine Learning

## Description
This project aims to predict whether an individual is suffering from depression using a dataset from Zindi. The dataset includes survey responses related to mental health in East Africa. We employ machine learning models to achieve this goal and provide a user-friendly web interface to input data and get predictions.

## Motivation
The motivation for this project is to leverage machine learning techniques to assist in the early diagnosis of depression, which can lead to timely and effective interventions. Early detection of mental health issues is crucial for improving the quality of life and health outcomes of individuals.

## Project Structure
- `app.py`: Flask application to serve the web interface and handle predictions.
- `templates/`: Contains the HTML template (`index.html`) for the web interface.
- `model.pkl`: The trained machine learning model serialized using joblib.
- `README.md`: Project documentation.
- `Early Diagnosis of Depression.pdf`: Contains the Capstone Project documentation.
- `Early Diagnosis of Depression Using Machine Learning.ipynb`: Jupyter Notebook with detailed analysis and code.


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

## Results
Three machine learning models were evaluated: K-Nearest Neighbors (KNN), Decision Tree (DT), and Support Vector Machine (SVM). The SVM model demonstrated the best performance with an accuracy of 83.33% and an ROC AUC score of 83.33%, making it the most effective model for predicting depression in this dataset. The KNN model also performed well, while the DT model showed slightly lower performance.

| Model | Train Score (%) | Accuracy (%) | ROC AUC (%) |
|-------|-----------------|--------------|-------------|
| KNN   | 84.35           | 81.94        | 81.94       |
| DT    | 86.05           | 77.78        | 77.78       |
| SVM   | 88.10           | 83.33        | 83.33       |

## Project Definition
The aim of this project was to predict whether an individual is suffering from depression using machine learning models. The project involved data preprocessing, feature selection, model training, and evaluation.

## Analysis
- **Data Preprocessing**: Missing values were handled by dropping columns and rows with high percentages of missing data. The dataset was then normalized using Robust Scaler.
- **Feature Selection**: The SelectKBest method was used to identify the most important features.
- **Model Training**: Three machine learning algorithms were trained and evaluated: K-Nearest Neighbors, Decision Tree, and Support Vector Machine.
- **Evaluation**: Models were evaluated based on accuracy, ROC AUC score, and confusion matrices. Hyperparameter tuning was performed using GridSearchCV.

## Conclusion
The SVM model outperformed the other models in terms of accuracy and ROC AUC score, making it the most effective model for predicting depression in this dataset. The project demonstrated the potential of machine learning in providing early diagnosis of depression, which can significantly impact treatment outcomes and quality of life.

## License
This project was completed as part of the Udacity Data Scientist Nanodegree program.

## Additional Documentation
The file `Early Diagnosis of Depression.pdf` contains the detailed Capstone Project documentation, providing a comprehensive overview of the project's objectives, methodology, results, and conclusions.

## Acknowledgements
- This project is part of the Udacity Data Scientist Nanodegree program.
- Special thanks to Zindi for providing the dataset used in this project.
- Thanks to various online resources such as StackOverflow and Kaggle for their valuable insights and solutions.
