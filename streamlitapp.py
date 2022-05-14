import streamlit as st
st.write(
    """
# 📊 A/B Testing App
Upload your experiment results to see the significance of your A/B test.
"""
)

uploaded_file = st.file_uploader("Upload CSV", type=".csv")
