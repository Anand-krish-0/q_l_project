import numpy as np
import pandas as pd
import streamlit as st
import pickle

def load_model():
    with open("",'rb') as file:
        data = pickle.load(file)
        return data
data = load_model()
model = data['model']

def predict_page():
    #[age, sex, bmi, children, smoker, region]

    x1 = st.selectbox("Age :", [])
    x2 = st.selectbox("Gender :", [])
    x3 = st.text_input("BMI :", )
    x4 = st.text_input("No.of Children :")
    x5 = st.selectbox("Smoker :", [])
    x6 = st.selectbox("Region :", [])

    ok = st.button("Predict")
    if ok:
        input = pd.DataFrame({"age":x1, "sex":x2, "bmi":x3, "children":x4, "smoker":x5, "region":x6})
        # encoding the categorical values
        # encoding sex column
        input.replace({'sex':{'male':0, 'female':1}}, inplace=True)

        # encoding smoker column
        input.replace({'smoker':{'yes':0, 'no':1}}, inplace=True)

        # encoding region column
        input.replace({'region':{'southeast':0, 'southwest':1, 'northeast':2, 'northwest':3}}, inplace=True)

        pre_data = input.values

        prediction = model.predict(pre_data)

        st.success("The Insurance Cost in USD ", prediction[0])

