Title: Employee Attrition Prediction Using Logistic Regression

Description: This project aims to predict employee attrition using logistic regression. By analyzing various features of employees, we can identify patterns that lead to attrition and help organizations retain their valuable workforce.

Acknowledgments:
Data used for this Project -> IBM HR Analytics Employee Attrition & Performance
Machine learning library used for model training -> Scikit-Learn

Project Directory Structure:
├── Attrition <- Project Main Directory
│   ├── data <- data in originnal format
|   |   ├── HR_Employee_Attrition <- The original, immutable data dump
|   ├── notebooks
|   |   ├── 01_ImportPackage.pynb <- Different libraries used  
|   |   ├── 02_DataCleaning.pynb <- includes data cleaning process
|   |   ├── 03_EDA.pynb <- contains univariate analysis
|   |   ├── 04_Bi_variate.pynb <- contains bi-variate analysis
|   |   ├── 05_HypothesisTesting.pynb <- contains hypothesis testing methods  
|   |   ├── 06_TrainModel.pynb <- includes model oon train data
|   |   ├── 07_TestModel.pynb <- includes model fit on test data  
|   |   ├── 08_ModelEvaluation.pynb <- includes model evaluation methods
|   |   ├── 09_Recommendations.pynb <- includes conclusion and recommendations
|   ├── src
|   |   ├── data_processing
|   |   |   ├── 01_ImportPackage.py
|   |   |   ├── 02_DataCleaning.py
|   |   |   ├── 03_EDA.py
|   |   |   ├── 04_Bi_variate.py
|   |   |   ├── 05_HypothesisTesting.py
|   |   ├── model
|   |   |   ├── 06_TrainModel.py
|   |   |   ├── 07_TestModel.py
|   |   |   ├── 08_ModelEvaluation.py
|   |   |   ├── 09_Recommendations.py
│   ├── Setup.py
│   ├── README.md <- For anyone using this project
│   ├── License <- This project is licensed under the MIT License. See the LICENSE file for details.
│   ├── .gitignore

Results:
The logistic regression model predicts whether an employee will leave the company based on various features. The performance of the model is evaluated using metrics such as accuracy, precision, recall, and F1-score.