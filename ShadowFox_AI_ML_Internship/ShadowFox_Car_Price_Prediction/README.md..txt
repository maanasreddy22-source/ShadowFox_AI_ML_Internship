# Car Selling Price Prediction

## Project Overview
This project was developed as part of the ShadowFox AI/ML Engineer Internship.

The main objective is to build a Machine Learning model that predicts the selling price of a used car based on its details.

## Technologies Used
- Python
- Google Colab
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Gradio
- Joblib

## Dataset Information
The dataset contains information about used cars.

**Dataset features:**
- Car Name
- Year
- Selling Price
- Present Price
- Kilometers Driven
- Fuel Type
- Seller Type
- Transmission
- Previous Owners

Dataset size:
- Original records: 301
- Records after removing duplicates: 299
- Features used for prediction: 11

## Project Workflow

1. Data Collection
2. Data Exploration
3. Data Cleaning
4. Handling Duplicate Records
5. One-Hot Encoding
6. Feature Selection
7. Train-Test Split
8. Model Training
9. Model Evaluation
10. Random Forest Comparison
11. Hyperparameter Tuning
12. Final Price Prediction
13. Gradio Web Application

## Machine Learning Algorithms

### 1. Linear Regression
Used to predict the selling price based on the selected car features.

### 2. Random Forest Regression
Used as a second model to compare prediction performance.

### 3. Hyperparameter Tuning
GridSearchCV was used to find suitable Random Forest parameters.

## Model Evaluation

The Linear Regression model achieved the following results:

| Metric | Value |
|---|---:|
| MAE | 1.4729 |
| MSE | 6.3708 |
| RMSE | 2.5240 |
| R² Score | 0.7528 |

Linear Regression performed better than the Random Forest models on the test dataset.

## Sample Prediction

Input:
- Year: 2018
- Present Price: 8.5 lakhs
- Kilometers Driven: 30,000
- Previous Owners: 0
- Fuel: Petrol
- Seller: Individual
- Transmission: Manual

Predicted Selling Price: **₹5.20 lakhs**

## Gradio Application

A simple web application was developed using Gradio.

Users can enter car details and receive an estimated selling price.

Application file: `app/day26_car_price_app.py`

## Project Folder Structure

```text
ShadowFox_Car_Price_Prediction/
│
├── notebooks/
├── models/
├── app/
├── reports/
└── README.md
```

## How to Run the Project

1. Install the required Python libraries:

```bash
pip install pandas numpy scikit-learn gradio joblib
```

2. Keep `car_price_prediction_model.pkl` and the application file in their respective project folders.

3. Run the application from the project root directory:

```bash
python app/day26_car_price_app.py
```

## Conclusion

This project demonstrates how Machine Learning can be used to estimate used-car selling prices.

Linear Regression achieved the best test performance among the models evaluated. A Gradio application was also developed to make predictions through a simple user interface.

## Internship

**Organization:** ShadowFox  
**Domain:** Artificial Intelligence and Machine Learning  
**Project:** Car Selling Price Prediction