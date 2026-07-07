import streamlit as st

st.set_page_config(
    page_title="Airline Customer Satisfaction",
    page_icon="✈️",
    layout="centered",
)

st.title("Airline Customer Satisfaction Prediction")

st.markdown(
    """
    Welcome! This app is based on the Group 03 airline passenger satisfaction project.
    The dataset contains roughly **130,000 records** and **24 features** covering
    demographics, flight information, and inflight service ratings.
    """
)

st.header("Project Overview")

st.write(
    """
    We trained and evaluated several machine learning models to predict whether a
    passenger is **satisfied** or **neutral/dissatisfied** with their flight experience.
    """
)

st.subheader("Models compared")
st.markdown(
    """
    - **Random Forest** — AUC ≈ 0.994
    - **Decision Tree** — AUC ≈ 0.946
    - **Lasso Logistic Regression** — AUC ≈ 0.927
    - **Ridge Logistic Regression** — AUC ≈ 0.908
    - **Plain Logistic Regression** — AUC ≈ 0.751
    - **Elastic Net** — AUC ≈ 0.641
    """
)

st.subheader("Key drivers of satisfaction")
st.write(
    """
    The most important features turned out to be service-quality factors such as
    **Type of Travel**, **Inflight Wi-Fi Service**, **Online Boarding**, **Seat Comfort**,
    and **Class** — more than delays alone.
    """
)

st.sidebar.title("Navigation")
st.sidebar.info(
    """
    This is a starter version of the app.
    More interactive pages — data exploration, visualizations, and live prediction —
    will be added next.
    """
)

st.info("🚧 Interactive features are coming soon!")
