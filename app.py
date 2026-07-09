import json
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


@st.cache_data
def load_feature_selection_results():
    with open("feature_selection_results.json") as f:
        return json.load(f)


@st.cache_data
def load_feature_comparison_results():
    with open("feature_comparison_results.json") as f:
        return json.load(f)




# ---------------------------------------------------------------------------
# Overview page
# ---------------------------------------------------------------------------
def show_overview():
    # Hero header
    st.title("Airline Customer Satisfaction Prediction")
    st.markdown(
        """
        <div style="background: linear-gradient(90deg, #1f2937 0%, #111827 100%); 
                    padding: 1.25rem 1.5rem; border-radius: 12px; 
                    border-left: 5px solid #3b82f6; margin-bottom: 1.5rem;">
            <h3 style="margin: 0; color: #f9fafb;">
                Predicting passenger satisfaction from flight experience data
            </h3>
            <p style="margin: 0.5rem 0 0 0; color: #d1d5db;">
                Built on roughly <strong>130,000 airline records</strong> and
                <strong>24 features</strong> covering demographics, flight info,
                and inflight service ratings.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Quick stats cards
    c1, c2, c3, c4 = st.columns(4)
    c1.metric(label="Records", value="~130K")
    c2.metric(label="Features", value="24")
    c3.metric(label="Best AUC", value="0.994")
    c4.metric(label="Top Model", value="Random Forest")

    st.divider()

    # Project overview
    st.header("Project Overview")
    st.write(
        """
        I trained and evaluated several machine learning models to predict whether a
        passenger is **satisfied** or **neutral/dissatisfied** with their flight experience.
        The goal is to understand which parts of the journey matter most to passengers.
        """
    )

    # Models compared
    st.subheader("Models compared")
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

    col_table, col_chart = st.columns([2, 3])
    with col_table:
        st.dataframe(
            metrics.style.format({"AUC": "{:.3f}"}).background_gradient(
                subset=["AUC"], cmap="Greens"
            ),
            use_container_width=True,
            hide_index=True,
        )

    with col_chart:
        fig, ax = plt.subplots(figsize=(8, 4))
        bar_colors = [
            "#22c55e" if score == metrics["AUC"].max() else "#3b82f6"
            for score in metrics["AUC"]
        ]
        ax.barh(metrics["Model"], metrics["AUC"], color=bar_colors)
        ax.set_xlim(0, 1)
        ax.set_xlabel("ROC-AUC")
        ax.invert_yaxis()
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        st.pyplot(fig)

    st.info(
        "Random Forest came out on top, but the high scores also reflect that many "
        "predictive features are service ratings collected alongside the satisfaction label. ",
        icon="💡",
    )

    st.divider()

    # Key drivers
    st.subheader("Key drivers of satisfaction")
    st.write(
        """
        The most important features turned out to be service-quality factors — more than delays alone:
        """
    )

    drivers = [
        "Type of Travel",
        "Inflight Wi-Fi Service",
        "Online Boarding",
        "Seat Comfort",
        "Class",
    ]
    driver_cols = st.columns(len(drivers))
    for col, driver in zip(driver_cols, drivers):
        col.markdown(
            f"""
            <div style="background-color: #1f2937; padding: 0.75rem; 
                        border-radius: 8px; text-align: center; 
                        border: 1px solid #374151; margin-bottom: 0.5rem;">
                <span style="color: #60a5fa; font-weight: 600;">{driver}</span>
            </div>
            """,
            unsafe_allow_html=True,
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
        st.subheader("Satisfaction by top service ratings")
        top_service_features = [
            "Online_boarding",
            "Inflight_wifi_service",
            "Seat_comfort",
            "Inflight_entertainment",
        ]
        fig, axes = plt.subplots(2, 2, figsize=(11, 9))
        axes = axes.flatten()
        for idx, feature in enumerate(top_service_features):
            sns.countplot(
                x=df[feature],
                hue=df["satisfaction"],
                palette="Paired",
                ax=axes[idx],
            )
            axes[idx].set_title(
                f"Satisfaction by {feature.replace('_', ' ')}", fontsize=11
            )
            axes[idx].set_xlabel(feature.replace("_", " "), fontsize=10)
            axes[idx].set_ylabel("Count", fontsize=10)
            axes[idx].legend(title="Satisfaction", fontsize=7)
        plt.tight_layout(pad=3.0)
        st.pyplot(fig)

# ---------------------------------------------------------------------------
# Feature Selection page
# ---------------------------------------------------------------------------
def show_feature_selection():
    st.title("Feature Selection")
    st.write(
        """
        Multiple feature selection methods were applied to identify the most predictive
        variables for passenger satisfaction. This page compares the features selected
        by each method and shows which ones consistently appeared across techniques.
        """
    )

    st.warning(
        "These selected feature sets were used for insight and interpretation. The models on "
        "the Model Performance page and the predictor below were trained on the full set of "
        "features, not on a reduced subset.",
        icon="⚠️",
    )

    st.subheader("Impact of feature selection on Random Forest")
    comparison = load_feature_comparison_results()
    comparison_df = pd.DataFrame(
        {
            "Feature set": [
                "All features",
                "Frequently selected (6 features)",
                "Intersection of all methods (4 features)",
            ],
            "Feature count": [
                comparison["all_features"]["feature_count"],
                comparison["frequent_selected"]["feature_count"],
                comparison["intersection"]["feature_count"],
            ],
            "Accuracy": [
                comparison["all_features"]["accuracy"],
                comparison["frequent_selected"]["accuracy"],
                comparison["intersection"]["accuracy"],
            ],
            "AUC": [
                comparison["all_features"]["auc"],
                comparison["frequent_selected"]["auc"],
                comparison["intersection"]["auc"],
            ],
        }
    )

    st.dataframe(
        comparison_df.style.format({"Accuracy": "{:.4f}", "AUC": "{:.4f}"}).background_gradient(
            subset=["Accuracy", "AUC"], cmap="Greens"
        ),
        use_container_width=True,
        hide_index=True,
    )

    st.info(
        "Using all 22 features gives the highest accuracy and AUC. The selected feature sets "
        "perform slightly worse but are much simpler. This is why the deployed predictor uses "
        "all features.",
        icon="📊",
    )

    results = load_feature_selection_results()
    model_data = load_model()
    feature_names = model_data["feature_names"]

    method_names = {
        "chi_square": "Chi-Square",
        "wrapper": "Wrapper (SelectFromModel RF)",
        "random_forest_top10": "Random Forest Top 10",
        "permutation": "Permutation Importance",
        "decision_tree_top10": "Decision Tree Top 10",
        "rfe": "Recursive Feature Elimination",
        "rfecv": "RFE with Cross-Validation",
    }

    # Comparison table: features selected by each method
    comparison_df = pd.DataFrame(index=feature_names)
    for key, label in method_names.items():
        comparison_df[label] = [1 if f in results[key] else 0 for f in feature_names]

    st.subheader("Feature selection comparison")
    st.dataframe(
        comparison_df.style.background_gradient(subset=list(method_names.values()), cmap="Greens"),
        use_container_width=True,
    )

    # Random Forest feature importance
    st.subheader("Random Forest feature importance")
    importance_df = pd.DataFrame(
        {
            "Feature": model_data["feature_names"],
            "Importance": model_data["feature_importances"],
        }
    ).sort_values("Importance", ascending=True)

    fig, ax = plt.subplots(figsize=(8, 6))
    bar_colors = [
        "#22c55e" if imp == importance_df["Importance"].max() else "#3b82f6"
        for imp in importance_df["Importance"]
    ]
    ax.barh(importance_df["Feature"], importance_df["Importance"], color=bar_colors)
    ax.set_xlabel("Importance")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    st.pyplot(fig)

    # Consistent features across methods
    st.subheader("Consistently selected features")
    method_lists = [results[key] for key in method_names.keys()]
    intersection = set(method_lists[0])
    for method_list in method_lists[1:]:
        intersection = intersection.intersection(set(method_list))

    union = set()
    for method_list in method_lists:
        union = union.union(set(method_list))

    col_int, col_union = st.columns(2)
    with col_int:
        st.write("**Selected by every method**")
        for feature in sorted(intersection):
            st.write(f"- {feature}")

    with col_union:
        st.write("**Selected by at least one method**")
        for feature in sorted(union):
            st.write(f"- {feature}")


# ---------------------------------------------------------------------------
# Model Performance page
# ---------------------------------------------------------------------------
def show_performance():
    st.title("Model Performance")

    st.write(
        """
        The models below were trained and evaluated on the **full set of features**.
        Feature selection was used to understand which variables matter most, but the
        final model comparison here uses all available inputs.
        """
    )

    col_auc, col_acc = st.columns(2)
    with col_auc:
        st.info(
            "**AUC (also called ROC-AUC)** tells us how often the model ranks a satisfied "
            "passenger higher than a dissatisfied one. Imagine picking one satisfied and one "
            "dissatisfied passenger at random. AUC is the chance the model gives the satisfied "
            "passenger a higher score. 1.0 means perfect, 0.5 means coin flip.",
            icon="📈",
        )
    with col_acc:
        st.info(
            "**Accuracy** is the percentage of passengers the model labeled correctly. "
            "If the model looks at 100 passengers and gets 96 right, accuracy is 96%. "
            "It is simple but can be misleading if one class is much bigger than the other.",
            icon="🎯",
        )

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
        ax.set_xlabel("AUC")
        st.pyplot(fig)

    st.subheader("Random Forest on held-out test set")
    st.write(
        "A held-out test set is data that was kept separate from training so the model never saw it "
        "while learning. Using it for the final evaluation gives a more realistic estimate of how "
        "the model would perform on new passengers."
    )
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

    st.info(
        "This predictor uses the Random Forest model trained on all available features, "
        "which achieved the highest AUC in the comparison.",
        icon="🤖",
    )

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
# Navigation
# ---------------------------------------------------------------------------
overview_page = st.Page(show_overview, title="Overview", icon="✈️")
eda_page = st.Page(show_eda, title="Data Exploration", icon="📊")
feature_page = st.Page(show_feature_selection, title="Feature Selection", icon="🔍")
performance_page = st.Page(show_performance, title="Model Performance", icon="📈")
predict_page = st.Page(show_prediction, title="Predict Satisfaction", icon="🎯")

pg = st.navigation(
    [overview_page, eda_page, feature_page, performance_page, predict_page]
)
pg.run()
