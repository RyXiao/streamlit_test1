import streamlit as st
import pandas as pd
st.write(
    """
# Shanghai COVID Curve
Upload your Shanghai COVID with data and cases to see the curve.
"""
)

uploaded_file = st.file_uploader("Upload CSV", type=".csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.line_chart(df)
