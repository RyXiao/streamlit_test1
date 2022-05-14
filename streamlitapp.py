import streamlit as st
import pandas as pd
import altair as alt


st.write(
    """
# Shanghai COVID Curve
Upload your Shanghai COVID with data and cases to see the curve.
"""
)

uploaded_file = st.file_uploader("Upload EXCEL XLSX FILE", type=".XLSX")

use_example_file = st.checkbox(
    "Use example file", False, help="Use in-built example file to demo the app"
)


# If CSV is not uploaded and checkbox is filled, use values from the example file
# and pass them down to the next if block
if use_example_file:
    uploaded_file = "Shanghai_COVID.XLSX"


if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.dataframe(df)
