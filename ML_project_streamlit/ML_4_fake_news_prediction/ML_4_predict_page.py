import numpy as np
import pandas as pd
import streamlit as st
import pickle

def load_model():
    with open('fake_news_prediction_saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

port_stem = data['port_stem']


#[title,author,text]	
title = st.text_input("Enter the title of the news: ")
author = st.text_input("Enter the author of the news: ")
text = st.text_input("Enter the text of the news: ")

