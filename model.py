#import the libraries

import pandas as pd
import streamlit as st
import joblib

#Model Import

model = joblib.load("model.h5")

#Application

st.title("Heart Disease Prediction Model")

age = st.slider("Select Your Age")

cigsPerDay = st.number_input("Enter No.of Cigarettes Per Day")

gender = st.radio("Select Your Gender",["Male","Female"],horizontal=True)

if gender=="Male":
    gender=1
else:
    gender=0

BPMeds = st.radio("Do you take BP Medicines?",["Yes","No"],horizontal=True)

if BPMeds == "Yes":
    BPMeds=1.0
else:
    BPMeds=0.0

prevStroke = st.radio("Do you have any prevalent stroke?",["Yes","No"],horizontal=True)

if prevStroke == "Yes":
    prevStroke=1
else:
    prevStroke=0

prevHyp = st.radio("Do you have any prevalent hypertension?",["Yes","No"],horizontal=True)


if prevHyp == "Yes":
    prevHyp=1
else:
    prevHyp=0

diabetes = st.radio("Do you have any prevalent diabetes?",["Yes","No"],horizontal=True)


if diabetes == "Yes":
    diabetes=1
else:
    diabetes=0

totChol = st.number_input("Enter your cholestrol level")

sysBP = st.number_input("Enter your systole blood pressure level")

diaBP = st.number_input("Enter your diastole blood pressure level")

bmi = st.number_input("Enter Your Body Mass Index Value")

heartRate = st.number_input("Enter Your Heart Beat Rate Per Minute")

button = st.button("Predict")

data = [[gender,age,cigsPerDay,BPMeds,prevStroke,prevHyp,diabetes,totChol,sysBP,diaBP,bmi,heartRate]]

if button:
    prediction=model.predict(data)
    if prediction[0]==0: 
        st.success("You are not at risk of heart disease")
    else:
        st.warning("You are at risk of heart disease")




