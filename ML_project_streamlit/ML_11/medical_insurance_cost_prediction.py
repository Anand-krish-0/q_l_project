from ml11_predict_page import predict_page
from ml11_explore_page import explore_page
import streamlit as st


st.title("Medical Insurance Cost Prediction")
# Create tabs
tab1, tab2 = st.tabs(["Prediction", "Explore"])

# Display the content of each tab
with tab1:
    predict_page()

with tab2:
    explore_page()
