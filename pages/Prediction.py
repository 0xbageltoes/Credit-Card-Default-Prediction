import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import image
import joblib
from lightgbm import LGBMClassifier
import os

st.title("Credit Card Defaulter Prediction")
file_dir=os.path.dirname(os.path.abspath(__file__))
parent_dir=os.path.join(file_dir,os.pardir)
file_of_interest=os.path.join(parent_dir,"model.joblib")
model=joblib.load(file_of_interest)

Sex=["Male","Female"]
Education=["Graduate school","University","High school","Others"]
Marital=["Married","Single","Others"]

with st.form('user_inputs'):
    sex=st.selectbox("Sex",("Male","Female"))
    education=st.selectbox("Education",("Graduate school","University","High school","Others"))
    marital=st.selectbox("Marital Status",("Married","Single","Others"))
    age=st.slider("Age of Person", min_value=20, max_value=80, value=30, step=5)
    limit=st.slider("Credit Limit", min_value=10000.0, max_value=1000000.0, value=100000.0, step=1000.0)
    
    st.markdown("""**History of Past Payment Delay**""")
    col1,col2,col3=st.columns(3)
    with col1:
        delay1=st.selectbox("Payment Delay 1", list(range(10)),index=0)
    with col2:
        delay2=st.selectbox("Payment Delay 2", list(range(10)),index=0)
    with col3:
        delay3=st.selectbox("Payment Delay 3", list(range(10)),index=2)


    st.markdown("""**Amount of Bill statement (dollars) for past 3 months**""")
    col1,col2,col3=st.columns(3)
    with col1:
        bill1=st.slider("Bill Amount 1", min_value=0.0, max_value=340000.0, value=10000.0, step=1000.0)
    with col2:
        bill2=st.slider("Bill Amount 2", min_value=0.0, max_value=340000.0, value=200000.0, step=1000.0)
    with col3:
        bill3=st.slider("Bill Amount 3", min_value=0.0, max_value=340000.0, value=100000.0, step=1000.0)
    
    st.markdown("""**Amount of Payment statement (dollars) for past 3 months**""")
    col1,col2,col3=st.columns(3)
    with col1:
        payam1=st.slider("Payment Amount 1", min_value=0.0, max_value=80000.0, value=9000.0, step=1000.0)
    with col2:
        payam2=st.slider("Payment Amount 2", min_value=0.0, max_value=80000.0, value=12000.0, step=1000.0)
    with col3:
        payam3=st.slider("Payment Amount 3", min_value=0.0, max_value=80000.0, value=25000.0, step=1000.0)


    click=st.form_submit_button()

if click:
    age=np.digitize(age,bins=range(20,85,5))
    data=np.array([[limit,(Sex.index(sex)+1),(Education.index(education)+1),(Marital.index(marital)+1),age,
                   delay1,delay2,delay3,bill1,bill2,bill3,payam1,payam2,payam2]])
    
    proba=model.predict_proba(data)[0][1]
    if proba<=0.201:
        st.error(f"Customer will default on payments with probability")
    else:
        st.success(f"Customer will not default on payments with probability")
