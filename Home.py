import streamlit as st

st.set_page_config(
    page_title="Heart Disease Matters",
    page_icon=":information_source:",
)

st.write("# ♥️ Matters of the Heart! ♥️")

st.sidebar.success("Select a page above for more information.")

st.markdown(
    """
    Heart disease is the [leading cause of death in the United States](https://www.cdc.gov/heartdisease/facts.htm). 
    The term “heart disease” refers to several types of heart conditions. 
    In the United States, the most common type of heart disease is coronary artery disease (CAD), which can lead to heart attack. 
    You can greatly reduce your risk for heart disease through lifestyle changes and, in some cases, medicine.
    ### Learn more about heart disease?
    - Check out [CDC Website](https://www.cdc.gov/heartdisease/index.htm)
    *The data source is from CDC.
"""
)