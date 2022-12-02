import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
from altair import datum
import math


st.sidebar.header("Heart Disease Risk Factors")

age = st.sidebar.selectbox('Age', ['18-24','25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80 or older'])
sex = st.sidebar.selectbox('Sex', ['Male', 'Female'])
race = st.sidebar.selectbox('Race', ['White', 'Black', 'Asian', 'Hispanic', 'American Indian/Alaskan Native', 'Other'])
bmi= st.sidebar.number_input('Body Mass Index (BMI)', min_value=1, value=20, step=1)
sleep = st.sidebar.slider('How many hours on average do you sleep per day?', min_value=0, max_value=24, step=1, value=8)
ghealth = st.sidebar.selectbox('How can you define your general health?', ['Excellent', 'Very good', 'Good', 'Fair', 'Poor'])
phealth = st.sidebar.slider('For how many days during the past 30 days was your physical health not good?',min_value=0, max_value=30,value=1)
mhealth = st.sidebar.slider('For how many days during the past 30 days was your mental health not good?', min_value=0, max_value=30, value=1)
sports = st.sidebar.selectbox('Have you played any sports (running, biking, etc.) in the past month?',['Yes', 'No'])
walk = st.sidebar.selectbox('Do you have serious difficulty walking or climbing stair?', ['Yes','No'],index=1)
smoke = st.sidebar.selectbox('Have you smoked at least 100 cigarettes in your entire life (approx. 5 packs)?',['Yes','No'],index=1)
alcohol = st.sidebar.selectbox('Do you have more than 14 drinks of alcohol (men) or  more than 7 (women) in a week?', ['Yes','No'], index=1)
stroke = st.sidebar.selectbox('Did you have a stroke?', ['Yes','No'], index=1)
diabete = st.sidebar.selectbox('Have you ever had diabetes?', ['Yes', 'No'],index=1)
asthama = st.sidebar.selectbox('Do you have asthma?', ['Yes', 'No'], index=1)
kidney = st.sidebar.selectbox('Do you have kidney disease?', ['Yes', 'No'], index=1)
skin = st.sidebar.selectbox('Do you have skin cancer?', ['Yes', 'No'],index=1)

if age == '18-24':
    intage=1
elif age == '25-29':
    intage=2
elif age == '30-34':
    intage=3
elif age == '35-39':
    intage=4
elif age == '40-44':
    intage=5
elif age == '45-49':
    intage=6
elif age == '50-54':
    intage=7
elif age == '55-59':
    intage=8
elif age == '60-64':
    intage=9
elif age == '65-69':
    intage=10
elif age == '70-74':
    intage=11
elif age == '75-79':
    intage=12
else:
    intage=13

if sex == 'Female':
    intsex=1
else:
    intsex=0

if race == 'Black':
    intBlack=1
    intAsian=0
    intOther=0
    intHispanic=0
    intWhite=0
elif race == 'Asian':
    intBlack=0
    intAsian=1
    intOther=0
    intHispanic=0
    intWhite=0
elif race == 'White':
    intBlack=0
    intAsian=0
    intOther=0
    intHispanic=0
    intWhite=1
elif race == 'Hispanic':
    intBlack=0
    intAsian=1
    intOther=0
    intHispanic=0
    intWhite=0
elif race == 'Other':
    intBlack=0
    intAsian=0
    intOther=1
    intHispanic=0
    intWhite=0
else:
    intBlack=0
    intAsian=0
    intOther=0
    intHispanic=0
    intWhite=0

if ghealth == 'Poor':
    intghealth=1
elif ghealth == 'Fair':
    intghealth=2
elif ghealth == 'Good':
    intghealth=3
elif ghealth == 'Very good':
    intghealth=4
else:
    intghealth=5

if sports=='Yes':
    intsports=1
else:
    intsports=0

if walk=='Yes':
    intwalk=1
else:
    intwalk=0

if smoke=='Yes':
    intsmoke=1
else:
    intsmoke=0

if alcohol=='Yes':
    intalcohol=1
else:
    intalcohol=0

if stroke=='Yes':
    intstroke=1
else:
    intstroke=0

if diabete=='Yes':
    intdiabete=1
else:
    intdiabete=0

if asthama=='Yes':
    intasthama=1
else:
    intasthama=0

if kidney=='Yes':
    intkidney=1
else:
    intkidney=0

if skin=='Yes':
    intskin=1
else:
    intskin=0

prob=math.exp(-3.4336342+0.0110256*bmi+0.3601919*intsmoke-0.2625697*intalcohol+1.0576796*intstroke+0.0018775*phealth
    +0.0048685*mhealth+0.2094884*intwalk-0.6929426*intsex+0.2709786*intage-0.0474116*intWhite-0.3098992*intBlack-0.4508379*intAsian
    -0.2120680*intHispanic-0.0207115*intOther+0.4632939*intdiabete-0.0239435*intsports-0.5020977*intghealth-0.0250345*sleep
    +0.2749699*intasthama+0.5497726*intkidney+0.1221977*intskin)/(1+math.exp(-3.4336342+0.0110256*bmi+0.3601919*intsmoke-0.2625697*intalcohol+1.0576796*intstroke+0.0018775*phealth
    +0.0048685*mhealth+0.2094884*intwalk-0.6929426*intsex+0.2709786*intage-0.0474116*intWhite-0.3098992*intBlack-0.4508379*intAsian
    -0.2120680*intHispanic-0.0207115*intOther+0.4632939*intdiabete-0.0239435*intsports-0.5020977*intghealth-0.0250345*sleep
    +0.2749699*intasthama+0.5497726*intkidney+0.1221977*intskin))

st.write("# Heart Disease Prediction")

st.write("### Heart Disease in the United States")

st.markdown(
    """
    - Heart disease is the leading cause of death for men, women, and people of most racial and ethnic groups in the United States.
    - One person dies every 34 seconds in the United States from cardiovascular disease.
    - About 697,000 people in the United States died from heart disease in 2020—that's 1 in every 5 deaths.
    - Heart disease cost the United States about $229 billion each year from 2017 to 2018. This includes the cost of health care services, medicines, and lost productivity due to death
"""
)

st.write("### Heart Disease Deaths Vary by Sex, Race, and Ethnicity")

st.markdown(
    """
    Heart disease is the leading cause of death for people of most racial and ethnic groups in the United States, including African American, American Indian, Alaska Native, Hispanic, and white men. 
    For women from the Pacific Islands and Asian American, American Indian, Alaska Native, and Hispanic women, heart disease is second only to cancer.
"""
)

st.write("### Americans at Risk for Heart Disease")

st.markdown(
    """
    [High blood pressure](https://www.cdc.gov/bloodpressure/index.htm), [high blood cholesterol](https://www.cdc.gov/cholesterol/index.htm), and smoking are key [risk factors](https://www.cdc.gov/heartdisease/risk_factors.htm) for heart disease.
"""
)

st.markdown(
    """
    Several other medical conditions and lifestyle choices can also put people at a higher risk for heart disease, including:
    - [Diabetes](https://www.cdc.gov/diabetes/basics/diabetes.html)
    - [Overweight and obesity](https://www.cdc.gov/obesity/index.html)
    - [Unhealthy diet](https://www.cdc.gov/healthyweight/healthy_eating/index.html)
    - [Physical inactivity](https://www.cdc.gov/physicalactivity/index.html)
    - [Excessive alcohol use](https://www.cdc.gov/alcohol/fact-sheets/alcohol-use.htm)
"""
)

st.write("### What's your probability for heart disease?")
st.markdown(
    """
    Scared? Concerns? Wondering if you are at high risk for heart disease? No worries. We are here to help. 💁
    Please fill out the fields 👈 and click the button 👇. 
"""
)

if st.button('Heart Disease Probabilty Prediction'):
    if prob <0.075: # Low: Less than a 7.5% risk.
        st.success(f"Awesome! You are at low risk with the heart disease probability: {format(prob,'.2%')}")
    elif (prob >0.075) & (prob <0.2): #Medium: A 7.5% to 19.9% risk.
        st.warning(f"Attention! You are at medium risk with the heart disease probability: {format(prob,'.2%')}")
    else: # High: More than a 20% risk
        st.error(f"Take action! You are at high risk with the heart disease probability: {format(prob,'.2%')}")
        st.write("### Prevent Heart Disease")
        st.markdown(
            """
            By living a healthy lifestyle, you can help keep your blood pressure, cholesterol, and blood sugar levels normal and lower your risk for heart disease and heart attack.
            - Choose Healthy Habits
                - Choose Healthy Foods and Drinks
                - Keep a Healthy Weight
                - Get Regular Physical Activity
                - Don't Smoke
            - Take Charge of Your Medical Conditions
                - Check Your Cholesterol
                - Control Your Blood Pressure
                - Manage Your Diabetes
                - Take Your Medication as Directed
                - Work with Your Health Care Team
            - More Information
                - [CDC](https://www.cdc.gov/heartdisease/prevention.htm)
                - [Million Hearts ABCS of Heart Health](https://millionhearts.hhs.gov/data-reports/factsheets/ABCS.html)
                - Vital Signs Topic: [Cardiovascular Diseases](https://www.cdc.gov/nccdphp/dnpao/index.html)
                - USDA [Center for Nutrition Policy and Promotion - Dietary Guidelines](https://www.nal.usda.gov/fnic/dietary-guidelines)
                - American Heart Association: [Monitoring Your Blood Pressure at Home](https://www.heart.org/en/health-topics/high-blood-pressure/understanding-blood-pressure-readings/monitoring-your-blood-pressure-at-home)
        """
        )

