# Project 6

## **Dataset** : Heart attack Analysis

- Age : Age of the patient
- Sex : Sex of the patient
- exang: exercise induced angina (1 = yes; 0 = no)
- ca: number of major vessels (0-3)
- cp : Chest Pain type chest pain type:
* Value 1: typical angina
* Value 2: atypical angina
* Value 3: non-anginal pain
* Value 4: asymptomatic
- trtbps : resting blood pressure (in mm Hg)
- chol : cholestoral in mg/dl fetched via BMI sensor
- fbs : (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
- rest_ecg : resting electrocardiographic results:
* Value 0: normal
* Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
* Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria

* thalach : maximum heart rate achieved
* output : 0= less chance of heart attack 1= more chance of heart attack


# Steps:
0. Data Preprocessing
    1. EDA Exploratory Data Analysis --> stats , Visualization
    2. Data Profiling
    3. Data Cleaning
    4. Feature Engineering
1. Use all classifiers (NN, LogReg, DT, RF, KNN) to classify the rows, if he/she has a chance for heat attach or not.
2. Use GridSearch to find the optimal hyper parameters for most best accuracy
3. Use Logging to show the different stages of the application



- Extension: Use PCA to reduce the features
- Delivery: Notebook or Application (10.01.2023 at 16:00)
