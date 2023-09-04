import streamlit as st
import os
from matplotlib import image

file_dir=os.path.dirname(os.path.abspath(__file__))
parent_dir=os.path.join(file_dir,os.pardir)
dir_of_interest=os.path.join(parent_dir,"findings")

st.title("Data Visualization")

#Class variable Distribution
st.subheader('Class Distribution')
image_path= os.path.join(dir_of_interest, "image1.png")
img = image.imread(image_path)
st.image(img)
st.markdown("""
            - There is imbalance in class distribution.
            - We will use sampling method, cost-sensitive learning to see if they increase the performance of algorithm.""")

#Numerical Variable Distribution
st.subheader('Numerical Variable Distribution')
image_path= os.path.join(dir_of_interest, "image2.png")
img = image.imread(image_path)
st.image(img)
st.markdown("""
             - Numerical variable have non-gaussian distribution, therefore we will use power transformer to transform \
               them to gaussian like.
             - As the LIMIT Balance increases the proportion of defaulters decreases, there is monotonically decreasing \
               ratio of defaulters with increasing LIMIT Balance.""")

st.subheader('Categorical Variable Distribution')
image_path= os.path.join(dir_of_interest, "image5.png")
img = image.imread(image_path)
st.image(img)
st.markdown("""
            - Women are more susceptible to defaulting then men as can be seen from data 53.8 percent female against 46.2\
              percent male.
            - Single person has lower defaulting ratio in comparison to married,divorced,live-in person as they have less\
              expenses and not responsible for family,children..""")

st.subheader('Bivariate Analysis between History of past payment, Amount of bill statement , Amount of previous payment \
             and default variable')
image_path= os.path.join(dir_of_interest, "image3.png")
img = image.imread(image_path)
st.image(img)
st.markdown("""
            - When BILL AMOUNT is negative,that means bank owns card holder money, with positive BILL AMOUNT the ratio of \
              defaulters increases with increase in BILL AMOUNT, larger the sum of money to be repayed more will the chances \
              of defaulting.
            - The Pay (Repayment Status) shows that with one month repayment delay, there is large increase in ratio of card \
              defaulting. The same pattern is exhibited by all Pay variables.
            - With increasing PAY AMOUNT the ratio of defaulting decreases, as the borrower is rapaying the amount preventing \
              bill amount from accumulating and becoming untenable.""")

st.subheader('Bivariate Analysis between History of past payment, Amount of bill statement  and Amount of previous payment.')
image_path= os.path.join(dir_of_interest, "image4.png")
img = image.imread(image_path)
st.image(img)
st.markdown("""
            - As the LIMIT BALANCE increases the BILL AMOUNT for defaulters have higher mean then BILL AMOUNT for non-defaulters,\
              while they have same distribution for lower LIMIT BALANCE(0-250000).
            - Card Holders with high PAY AMOUNT have lower default then with low PAY AMOUNT.""")