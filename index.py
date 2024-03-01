import pickle
import streamlit as st
import pandas as pd
import numpy as np


model = pickle.load(open('linearRegressionModel.pkl', 'rb'))
car_df = pd.read_csv('Cleaned_car_data.csv')
model_2=pickle.load(open('DecisionTreeRegressor_model.pkl', 'rb'))

def predict():
   score = model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                                      data=np.array([selected_car, selected_company, selected_year, kms_driven,
                                                     selected_fuel_type]).reshape(1, 5)))
   return str(np.round(score[0],decimals=2))

def predict_model2():
   score = model_2.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                                      data=np.array([selected_car, selected_company, selected_year, kms_driven,
                                                     selected_fuel_type]).reshape(1, 5)))
   return str(np.round(score[0],decimals=2))


st.header('Car Price Prediction System')
selected_company = st.selectbox("Select the Company", car_df['company'].unique(), index=None ,placeholder="Choose a Company")
filtered_cars = car_df.query('company == @selected_company')
selected_car = st.selectbox("Select the Model", filtered_cars['name'].unique())
#selected_year = st.selectbox("Select Year of Purchase", sorted(car_df['year'].unique()))
selected_year = st.selectbox("Select Year of Purchase", sorted(range(1990,2024)))
selected_fuel_type = st.selectbox("Select the Fuel Type", car_df['fuel_type'].unique())
kms_driven = st.number_input('Enter the Number of Killometres that the car has travelled')

submitted = st.button("Submit")
if submitted:
   st.write("LinearRegressionModel Predicted Price is: RS",predict())
   st.write("-----------------------------------------------------------")
   st.write("DecisionTreeRegressorModel Predicted Price is: RS", predict_model2())
