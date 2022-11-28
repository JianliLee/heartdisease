import streamlit as st
import pandas as pd
import altair as alt
import numpy as np


st.set_page_config(
    page_title="Risk Factors For Heart Disease",
    page_icon="📊",
)

st.write("# Risk Factors For Heart Disease")

st.write("### Do age and sex affect the risk of heart disease?")

st.markdown(
    """
   Heart disease is the number one killer of both men and women.
   Heart disease can happen at any age, but the risk goes up as you age.
"""
)

hd = pd.read_csv ('heart_2020_cleaned_JL.csv')

bar_age = alt.Chart(hd,title= "Age").mark_bar().encode(
    x="AgeCategory",
    y="count()", 
    
)

# bar_age = alt.Chart(hd,title= "Age").transform_joinaggregate(
#     Total='count()',
#     HDcount=len(hd[hd['HeartDisease']=='Yes'])
# ).transform_calculate(
#     PercentOfTotal="HDcount / Total"
# ).mark_bar().encode(
#     alt.X('PercentOfTotal:Q', axis=alt.Axis(format='.0%')),
#     y='AgeCategory'
# )

st.altair_chart(bar_age, use_container_width=True)

