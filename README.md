

# Credit Card Default Prediction

Credit Card payment default occurs when you fail to pay the Minimum Amount Due (MAD) on the credit card for a few consecutive months. Usually, the default notice is sent by the card issuer after 6 consecutive missed payments.

Consequences of Credit card payment default

Lawful Punishments
Suspended Credit Card Account
Detrimental Effect on Credit Score
High-Interest Rates
Asset Possession
In this project we classify customers as potential defaulters given personal and 6 months banking details.

## Dataset Features

- **Credit Limit**: Amount of the given credit (in dollars): it includes both the individual consumer credit and his/her family (supplementary) credit
- **Sex**: (1=male; 2=female)
- **Education**: (1=graduate school; 2=university; 3=high school; 4=other)
- **Marital Status**: (1=married; 2=single; 3=others)
- **Age**: years
- **History of past payment**: The measurement scale for the repayment status is: -1 = pay duly; 1 = payment delay for one month; 2 = payment delay for two months; . . .; 8 = payment delay for eight months; 9 = payment delay for nine months and above
- **Amount of bill statement**: (dollars) for past 6 months
- **Amount of previous payment** past 6 months
![](https://github.com/sudhanshu2198/Computer-Vision-using-Pytorch/blob/main/images/2.png)


**The main goal of this project is to develop a Credit Card Defaulter Prediction model and deploying the model using streamkit as an Web App.**

## 🔗 Links

- [Dataset](https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset)
- [Medium Article](https://medium.com/@sudhanshurastogi/credit-card-defaulter-prediction-79816add2deb)
- [Kaggle Notebook](https://www.kaggle.com/code/sudhanshu2198/credit-card-default-prediction)

## 🛠 Frameworks
Numpy, Pandas, Matplotlib, Seaborn, Scikit-learn, Imblearn, Xgboost, Lightgbm 

## Visualization


## Results

**The model is trained for 15 epochs using GPU Tesla P-100. It achieved weighted f1_score of 70% on validation dataset.**





