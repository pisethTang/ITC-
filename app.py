import pickle

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

# ---------------------------------------------------------------------------
# Page configuration
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Airline Customer Satisfaction",
    page_icon="✈️",
    layout="wide",
)

# ---------------------------------------------------------------------------
# Cached loaders
# ---------------------------------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("Dataset/output1.csv")
    df = df.drop(columns=["Unnamed: 0", "id"], errors="ignore")
    return df


@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)


# ---------------------------------------------------------------------------
# Navigation
# ---------------------------------------------------------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Overview", "Data Exploration", "Model Performance", "Predict Satisfaction"],
)

# ---------------------------------------------------------------------------
# Overview page
# ---------------------------------------------------------------------------
def show_overview():
    st.title("Airline Customer Satisfaction Prediction")

    st.markdown(
        """
        This app explores airline passenger satisfactions.
        The dataset contains roughly **130,000 records** and **24 features** covering
        demographics, flight information, and inflight service ratings.
        """
    )

    st.header("Project Overview")
    st.write(
        """
        I trained and evaluated several machine learning models to predict whether a
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


# ---------------------------------------------------------------------------
# Data Exploration page
# ---------------------------------------------------------------------------
def show_eda():
    st.title("Data Exploration")
    df = load_data()

    st.write(f"**Dataset shape:** {df.shape[0]:,} rows × {df.shape[1]} columns")
    with st.expander("Preview raw data"):
        st.dataframe(df.head(10), use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Target distribution")
        fig, ax = plt.subplots(figsize=(6, 4))
        df["satisfaction"].value_counts().plot.pie(
            autopct="%1.1f%%", startangle=90, ax=ax
        )
        ax.set_ylabel("")
        st.pyplot(fig)

    with col2:
        st.subheader("Numerical correlations")
        numerical_cols = [
            "Age",
            "Flight_Distance",
            "Departure_Delay_in_Minutes",
            "Arrival_Delay_in_Minutes",
        ]
        corr = df[numerical_cols].corr()
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.heatmap(corr, annot=True, cmap="YlGnBu", fmt=".2f", ax=ax)
        st.pyplot(fig)

    st.subheader("Feature importance from Random Forest")
    model_data = load_model()
    importance_df = pd.DataFrame(
        {
            "Feature": model_data["feature_names"],
            "Importance": model_data["feature_importances"],
        }
    ).sort_values("Importance", ascending=True)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.barh(importance_df["Feature"], importance_df["Importance"])
    ax.set_xlabel("Importance")
    st.pyplot(fig)


# ---------------------------------------------------------------------------
# Model Performance page
# ---------------------------------------------------------------------------
def show_performance():
    st.title("Model Performance")

    metrics = pd.DataFrame(
        {
            "Model": [
                "Random Forest",
                "Decision Tree",
                "Lasso Logistic Regression",
                "Ridge Logistic Regression",
                "Plain Logistic Regression",
                "Elastic Net",
            ],
            "AUC": [0.9936, 0.9460, 0.9268, 0.9079, 0.7507, 0.6413],
        }
    )

    col1, col2 = st.columns(2)
    with col1:
        st.dataframe(
            metrics.style.highlight_max(subset=["AUC"], color="green"),
            use_container_width=True,
        )

    with col2:
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.barh(metrics["Model"], metrics["AUC"])
        ax.set_xlim(0, 1)
        ax.set_xlabel("ROC-AUC")
        st.pyplot(fig)

    st.subheader("Random Forest on held-out test set")
    model_data = load_model()
    c1, c2 = st.columns(2)
    c1.metric("Accuracy", f"{model_data['test_accuracy']:.4f}")
    c2.metric("AUC", f"{model_data['test_auc']:.4f}")


# ---------------------------------------------------------------------------
# Prediction page
# ---------------------------------------------------------------------------
def show_prediction():
    st.title("Predict Passenger Satisfaction")

    model_data = load_model()
    model = model_data["model"]
    encoders = model_data["encoders"]
    feature_names = model_data["feature_names"]

    st.write("Adjust the passenger details below and click **Predict**.")

    with st.form("prediction_form"):
        col1, col2 = st.columns(2)

        with col1:
            gender = st.selectbox("Gender", encoders["Gender"].classes_)
            customer_type = st.selectbox(
                "Customer Type", encoders["Customer_Type"].classes_
            )
            age = st.slider("Age", 5, 80, 30)
            type_of_travel = st.selectbox(
                "Type of Travel", encoders["Type_of_Travel"].classes_
            )
            travel_class = st.selectbox("Class", encoders["Class"].classes_)
            flight_distance = st.number_input(
                "Flight Distance", min_value=0, max_value=10000, value=500
            )
            wifi = st.slider("Inflight Wi-Fi Service", 1, 5, 3)
            dep_arr_time = st.slider(
                "Departure/Arrival Time Convenient", 1, 5, 3
            )
            ease_online = st.slider("Ease of Online Booking", 1, 5, 3)
            gate_location = st.slider("Gate Location", 1, 5, 3)
            food_drink = st.slider("Food and Drink", 1, 5, 3)

        with col2:
            online_boarding = st.slider("Online Boarding", 1, 5, 3)
            seat_comfort = st.slider("Seat Comfort", 1, 5, 3)
            entertainment = st.slider("Inflight Entertainment", 1, 5, 3)
            onboard_service = st.slider("On-board Service", 1, 5, 3)
            leg_room = st.slider("Leg Room Service", 1, 5, 3)
            baggage = st.slider("Baggage Handling", 1, 5, 3)
            checkin = st.slider("Check-in Service", 1, 5, 3)
            inflight_service = st.slider("Inflight Service", 1, 5, 3)
            cleanliness = st.slider("Cleanliness", 1, 5, 3)
            dep_delay = st.number_input(
                "Departure Delay (min)", min_value=0, max_value=2000, value=0
            )
            arr_delay = st.number_input(
                "Arrival Delay (min)", min_value=0.0, max_value=2000.0, value=0.0
            )

        submitted = st.form_submit_button("Predict")

    if submitted:
        input_dict = {
            "Gender": gender,
            "Customer_Type": customer_type,
            "Age": age,
            "Type_of_Travel": type_of_travel,
            "Class": travel_class,
            "Flight_Distance": flight_distance,
            "Inflight_wifi_service": wifi,
            "Departure/Arrival_time_convenient": dep_arr_time,
            "Ease_of_Online_booking": ease_online,
            "Gate_location": gate_location,
            "Food_and_drink": food_drink,
            "Online_boarding": online_boarding,
            "Seat_comfort": seat_comfort,
            "Inflight_entertainment": entertainment,
            "On-board_service": onboard_service,
            "Leg_room_service": leg_room,
            "Baggage_handling": baggage,
            "Checkin_service": checkin,
            "Inflight_service": inflight_service,
            "Cleanliness": cleanliness,
            "Departure_Delay_in_Minutes": dep_delay,
            "Arrival_Delay_in_Minutes": arr_delay,
        }

        input_df = pd.DataFrame([input_dict])

        # Encode categorical columns the same way as training
        for col in ["Gender", "Customer_Type", "Type_of_Travel", "Class"]:
            input_df[col] = encoders[col].transform(input_df[col])

        # Ensure column order matches training
        input_df = input_df[feature_names]

        prob = model.predict_proba(input_df)[0]
        pred = model.predict(input_df)[0]

        if pred == 1:
            st.success(
                f"✅ Predicted: **Satisfied** (probability {prob[1]:.2%})"
            )
        else:
            st.error(
                f"⚠️ Predicted: **Neutral or Dissatisfied** (probability {prob[0]:.2%})"
            )


# ---------------------------------------------------------------------------
# Route to the selected page
# ---------------------------------------------------------------------------
if page == "Overview":
    show_overview()
elif page == "Data Exploration":
    show_eda()
elif page == "Model Performance":
    show_performance()
elif page == "Predict Satisfaction":
    show_prediction()
