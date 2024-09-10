import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load the dataset
insurance_dataset = pd.read_csv('d:/qtree projeccts/csv and excel files/machine learning project/medical insurance.csv')

def explore_page():

    st.title("Analytics")
    
    # Distribution of age values
    st.warning("Age Distribution")
    fig, ax = plt.subplots(figsize=(6,6))
    sns.histplot(insurance_dataset['age'], bins=30, kde=True, ax=ax)
    plt.title('Age Distribution')
    st.pyplot(fig)

    # Gender column (Sex Distribution)
    st.warning("Gender Distribution")
    fig, ax = plt.subplots(figsize=(6,6))
    sns.countplot(x='sex', data=insurance_dataset, ax=ax)
    plt.title('Gender Distribution')
    st.pyplot(fig)

    # BMI Distribution
    st.warning("BMI Distribution")
    fig, ax = plt.subplots(figsize=(6,6))
    sns.histplot(insurance_dataset['bmi'], bins=30, kde=True, ax=ax)
    plt.title('BMI Distribution')
    st.pyplot(fig)

    # Children column
    st.warning("Childrens Counting")
    fig, ax = plt.subplots(figsize=(6,6))
    sns.countplot(x='children', data=insurance_dataset, ax=ax)
    plt.title('Children')
    st.pyplot(fig)

    # Smoker column
    st.warning("No.of Smokers and Non-smokers")
    fig, ax = plt.subplots(figsize=(6,6))
    sns.countplot(x='smoker', data=insurance_dataset, ax=ax)
    plt.title('Smoker')
    st.pyplot(fig)

    # Region column
    st.warning("Region Counting")
    fig, ax = plt.subplots(figsize=(6,6))
    sns.countplot(x='region', data=insurance_dataset, ax=ax)
    plt.title('Region')
    st.pyplot(fig)

    # Distribution of charges
    st.warning("Distribution of Charges")
    fig, ax = plt.subplots(figsize=(6,6))
    sns.histplot(insurance_dataset['charges'], bins=30, kde=True, ax=ax)
    plt.title('Distribution of Charges')
    st.pyplot(fig)


