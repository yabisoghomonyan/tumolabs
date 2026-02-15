Employee Interview Acceptance Prediction
This project analyzes employee demographic and professional data to predict whether a candidate will be accepted for an interview. It utilizes data cleaning, interactive visualization, and multiple classification algorithms to determine the most effective predictive model.

#Project Overview
The goal of this study is to identify patterns in successful candidate profiles and build a machine learning pipeline that automates the screening process. We compare linear, distance-based, and probabilistic models to see which one handles recruitment data most accurately.

#Dataset Description
The analysis is based on logatta.csv, which includes:

Demographics: Age, Gender, Education, Marital Status.

Professional History: Business Travel frequency, Job Level, Years at Company, Training Times.

Target Variable: accepted for the interview (True/False).

#Data Preprocessing
Before modeling, the data underwent the following transformations:

Handling Categorical Data: Used OrdinalEncoder to convert text features into numerical formats.

Feature Scaling: Implemented StandardScaler to normalize the data, ensuring features like 'Age' and 'JobLevel' are on the same scale for models like KNN.

Data Splitting: Used an 80/20 split for training and testing to validate model performance.

#Visual Analysis
We utilized Plotly to create interactive subplots that compare candidate distributions.

Gender & Age Analysis: Investigated how age distribution differs between male and female candidates who were accepted.

Filtering Logic: Implemented complex Pandas filtering to isolate successful candidates for deeper feature inspection.

#Machine Learning & Comparison
We trained three distinct classifiers. Below is the comparison of their Confusion Matrices:

1. Logistic Regression (Conservative)
Result: [[260, 8], [21, 10]]

Performance: Very high precision. It rarely predicts "Accepted" incorrectly, but it misses a significant number of qualified candidates (21 False Negatives).

2. K-Neighbors Classifier (Balanced)
Result: [[246, 22], [17, 14]]

Performance: A middle-ground approach. It identifies more successful candidates than Logistic Regression but introduces more "False Alarms."

3. Gaussian Naive Bayes (Best Recall)
Result: [[229, 39], [3, 28]]

Performance: The strongest model for this use case. It only missed 3 qualified candidates. In recruitment, this is ideal because it ensures almost no talent is overlooked.

#Installation & Usage
Prerequisites
Ensure you have Python installed along with the following libraries:

Bash
pip install pandas numpy scikit-learn plotly scipy
Running the Project
Clone this repository.

Ensure logatta.csv is in the project directory.

Open code (1).ipynb in Jupyter Notebook or Google Colab.

Run all cells to generate the visualizations and model reports.

#Conclusion
While Logistic Regression offers the highest accuracy for "Non-Accepted" cases, Gaussian Naive Bayes is the recommended model for this project as it achieves the highest Recall (90%+), ensuring that the recruitment team captures as many potential interviewees as possible.
