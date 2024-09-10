import numpy as np
import pandas as pd
import streamlit as st
import pickle

def load_model():
    # Replace with the correct path to your model file
    with open("ML_project_streamlit\ML_11\med_ins_cost_prediction_model.pkl",'rb') as file:
        data = pickle.load(file)
        return data

data = load_model()
model = data['model']

def predict_page():

    st.title("Enter the details:")
    #[age, sex, bmi, children, smoker, region]

    x1 = st.text_input("Age :")
    x2 = st.selectbox("Gender :", ['Male','Female'])
    x3 = st.text_input("BMI :")
    x4 = st.text_input("No. of Children :")
    x5 = st.selectbox("Smoker :", ['Yes','No'])
    x6 = st.selectbox("Region :", ['southeast', 'southwest', 'northeast', 'northwest'])

    ok = st.button("Predict")
    if ok:
        # Convert inputs to appropriate types
        try:
            x1 = int(x1)  # Age as an integer
            x3 = float(x3)  # BMI as a float
            x4 = int(x4)  # Number of children as an integer
        except ValueError:
            st.error("Please enter valid numbers for Age, BMI, and Number of Children.")
            return

        # Create input DataFrame
        input_data = pd.DataFrame({"age": [x1], "sex": [x2], "bmi": [x3], "children": [x4], "smoker": [x5], "region": [x6]})
        
        # Encoding categorical values
        input_data.replace({'sex': {'Male': 1, 'Female': 0}}, inplace=True)
        input_data.replace({'smoker': {'Yes': 1, 'No': 0}}, inplace=True)
        input_data.replace({'region': {'southeast': 0, 'southwest': 1, 'northeast': 2, 'northwest': 3}}, inplace=True)

        # Prepare input for the model
        pre_data = input_data.values

        # Ensure the input data has the correct shape (e.g., 2D array)
        prediction = model.predict(pre_data)

        # Display the prediction
        st.success(f"The predicted Insurance Cost in USD: {prediction[0]}")


