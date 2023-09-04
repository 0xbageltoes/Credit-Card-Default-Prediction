import streamlit as st 
import os
from matplotlib import image

file_dir=os.path.dirname(os.path.abspath(__file__))
parent_dir=os.path.join(file_dir,os.pardir)
dir_of_interest=os.path.join(parent_dir,"findings")

st.title("Experiments Results")

#Algorithm Spot Checking
st.subheader('Algorithm Spot Checking')
image_path= os.path.join(dir_of_interest, "image7.png")
img = image.imread(image_path)
st.image(img)

image_path= os.path.join(dir_of_interest, "image8.png")
img = image.imread(image_path)
st.image(img)

st.markdown("""
            - LightGBM performs best among other models.
            - KNNClassifier performs poorly and is highly under confident for predicting positive class.
            - LightGBM,XGB,Random Forest, Logistic Regression classifiers have learned the underlying structure but are \
              under confident with high probabilities, therefore there performance can be increased by using probability \
              calibration.""")

#Cost Sensitive Learning
st.subheader('Cost Sensitive Learning')
image_path= os.path.join(dir_of_interest, "image9.png")
img = image.imread(image_path)
st.image(img)

image_path= os.path.join(dir_of_interest, "image10.png")
img = image.imread(image_path)
st.image(img)
st.markdown("""
            - Cost Sensitive Learning doesn't result into improvement in performance.
            - Also the class imbalance is not so severe, it is (80,20) therefore instead of accuracy we can use Gmeans to \
              estimate the performance of models.
            - Using cost sensitive learning results into XGBoost become overconfident and LightGBM becomes under confident. \
              It points to boosting algorithm propensity to over-fitting and performing poorly on test dataset.""")

#Features Importance
st.subheader('Features Importance')
image_path= os.path.join(dir_of_interest, "image11.png")
img = image.imread(image_path)
st.image(img)
st.markdown("""
            - All four models accord differnt importance to features, we can use ensembling to get a model that combines \
              the strength of each model""")

#Ensembling
st.subheader('Ensembling')
image_path= os.path.join(dir_of_interest, "image12.png")
img = image.imread(image_path)
st.image(img)

image_path= os.path.join(dir_of_interest, "image13.png")
img = image.imread(image_path)
st.image(img)
st.markdown("""
            - I have used optuna for hyperparameter tuning each model. The best hyper-parameters determined will be used \
              to build ensemble.
            - Though the ensemble model has lower performance then lgbm and xgb on train dataset, but have same performance \
              on test datasets, lower difference between train and test datasets performance.
            - Instead of average ensemble, we can also use weighted ensembling or stacking.""")













