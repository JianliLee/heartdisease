import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
from altair import datum


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

# bar_age = alt.Chart(hd,title= "Age").mark_bar().encode(
#     x="AgeCategory",
#     y="count()",
#     color = "HeartDisease"
# )

tab1, tab2 = st.tabs(['Age', 'Sex'])

selection = alt.selection_multi(fields=['HeartDisease'], bind='legend', init=[{'HeartDisease': 'Yes'}])

with tab1: 
    bar_age = alt.Chart(hd, title="Heart Disease Rate per Age Group").transform_aggregate(
        count='count()',
        groupby=['HeartDisease', 'AgeCategory']
    ).transform_joinaggregate(
        total='sum(count)',
        groupby=['AgeCategory']  
    ).transform_calculate(
        frac=alt.datum.count / alt.datum.total
    ).mark_bar().encode(
        x="AgeCategory:O",
        y=alt.Y('frac:Q',axis=alt.Axis(title="Percent", format=".2%")),
        color=alt.Color('HeartDisease:N', legend=None),
        tooltip=[
            alt.Tooltip('count:Q', title=f"Total records"),
            alt.Tooltip('frac:Q', title="Percentage", format='.2%')
        ]
    ).transform_filter(
        datum.HeartDisease == 'Yes'
    )

    label_age = bar_age.mark_text(
        align='center',
        baseline='line-bottom',
        dx=3  # Nudges text to right so it doesn't appear on top of the bar
    ).encode(
        text= alt.Text('frac:Q', format='.2%')
    )

    st.altair_chart(bar_age+label_age, use_container_width=True)

with tab2:
    bar_sex = alt.Chart(hd, title="Heart Disease Rate per Sex").transform_aggregate(
        count='count()',
        groupby=['HeartDisease', 'Sex']
    ).transform_joinaggregate(
        total='sum(count)',
        groupby=['Sex']  
    ).transform_calculate(
        frac=alt.datum.count / alt.datum.total
    ).mark_bar().encode(
        x="Sex:O",
        y=alt.Y('frac:Q', axis=alt.Axis(title="Percent", format=".2%")),
        color=alt.Color('HeartDisease:N', legend=None),
        tooltip=[
            alt.Tooltip('count:Q', title=f"Total records"),
            alt.Tooltip('frac:Q', title="Percentage", format='.2%')
        ]
    ).transform_filter(
        datum.HeartDisease == 'Yes'
    )

    label_sex = bar_sex.mark_text(
        align='center',
        baseline='line-bottom',
        dx=3  # Nudges text to right so it doesn't appear on top of the bar
    ).encode(
        text= alt.Text('frac:Q', format='.2%')
    )

    st.altair_chart(bar_sex+label_sex, use_container_width=True)  

st.write("### Do race and ethnicity affect the risk of heart disease?")

st.markdown(
    """
    Heart disease and stroke can affect anyone, but some groups are more likely to have conditions that increase their risk for cardiovascular disease.
    Heart disease is the leading cause of death for people of most racial and ethnic groups in the United States.
"""
)

bar_race = alt.Chart(hd, title="Heart Disease Rate per Race").transform_aggregate(
    count='count()',
    groupby=['HeartDisease', 'Race']
).transform_joinaggregate(
    total='sum(count)',
    groupby=['Race']  
).transform_calculate(
    frac=alt.datum.count / alt.datum.total
).mark_bar().encode(
    x=alt.X('frac:Q', axis=alt.Axis(title="Percent", format=".2%")),
    y=alt.Y('Race', sort=alt.EncodingSortField('frac', op='min', order='descending')),
    color=alt.Color('HeartDisease:N', legend=None),
    tooltip=[
        alt.Tooltip('count:Q', title=f"Total records"),
        alt.Tooltip('frac:Q', title="Percentage", format='.2%')
    ]
).transform_filter(
    datum.HeartDisease == 'Yes'
)

label_race = bar_race.mark_text(
    align='left',
    baseline='middle',
    dx=3  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text= alt.Text('frac:Q', format='.2%')
)

st.altair_chart(bar_race+label_race, use_container_width=True)

st.write("### Does Body Mass Index (BMI) affect the risk of heart disease?")

st.markdown(
    """
    BMI is a useful measure of overweight and obesity. It is calculated from your height and weight. 
    BMI is an estimate of body fat and a good gauge of your risk for diseases that can occur with more body fat.
    The higher your BMI, the higher your risk for certain diseases such  as heart disease, high blood pressure, type 2 diabetes.
"""
)

line_BMI = alt.Chart(hd, title="Heart Disease Rate per BMI").transform_bin(
    'BMIGroup', field='BMI', bin=alt.Bin(step=4)
).transform_aggregate(
    count='count()',
    groupby=['HeartDisease', 'BMIGroup']
).transform_joinaggregate(
    total='sum(count)',
    groupby=['BMIGroup']  
).transform_calculate(
    frac=alt.datum.count / alt.datum.total
).mark_line().encode(
    x=alt.X('BMIGroup:Q'),
    y=alt.Y('frac:Q', axis=alt.Axis(title="Percent", format=".0%")),
    color=alt.Color('HeartDisease:N', legend=None),
).transform_filter(
    datum.HeartDisease == 'Yes'
)

st.altair_chart(line_BMI, use_container_width=True)
