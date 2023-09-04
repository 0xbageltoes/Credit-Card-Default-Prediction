import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import image
import os

st.title("Introduction")
st.subheader("The main goal of this is to predict whether a customer will default on credit card bill payments given customer previous 6 months account history.")
st.write("With the growing number of credit card users, banks have been facing an escalating credit card default rate.\
          This increase in defaults causes losses to the financial institutions along with the card holders. As such data\
          analytics can provide solutions to tackle the current phenomenon and management of credit defaults. This project\
          discusses the implementation of an model which predicts if a given credit card holder has a probability of \
         defaulting in the following month, using their demographic data and behavioral data from the past 3 months.")

col1,col2=st.columns(2)
with col1:
    st.write("[Github Link](https://github.com/sudhanshu2198/Credit-Card-Default-Prediction)")
with col2:
    st.write("[Kaggle Link](https://www.kaggle.com/code/sudhanshu2198/credit-card-default-prediction)")

file_dir=os.path.dirname(os.path.abspath(__file__))
dir_of_interest = os.path.join(file_dir, "findings")
image_path= os.path.join(dir_of_interest, "image0.jpg")
img = image.imread(image_path)
st.image(img)
