import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score


def main():
    # Load the prepared dataset saved from the notebook
    df = pd.read_csv("Dataset/output1.csv")

    # Drop index-like columns that are not predictive
    df = df.drop(columns=["Unnamed: 0", "id"])

    # Label-encode categorical features so the tree model can use them
    categorical_cols = ["Gender", "Customer_Type", "Type_of_Travel", "Class"]
    encoders = {}
    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        encoders[col] = le

    # Convert the target to binary
    df["satisfaction"] = df["satisfaction"].map(
        {"satisfied": 1, "neutral or dissatisfied": 0}
    )

    X = df.drop(columns=["satisfaction"])
    y = df["satisfaction"]
    feature_names = X.columns.tolist()

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Train a Random Forest — the best-performing model from the project
    model = RandomForestClassifier(n_estimators=100, random_state=0, n_jobs=-1)
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]
    acc = accuracy_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_proba)

    print(f"Test Accuracy: {acc:.4f}")
    print(f"Test AUC:      {auc:.4f}")

    # Save everything the Streamlit app needs
    with open("model.pkl", "wb") as f:
        pickle.dump(
            {
                "model": model,
                "encoders": encoders,
                "feature_names": feature_names,
                "feature_importances": model.feature_importances_,
                "test_accuracy": acc,
                "test_auc": auc,
            },
            f,
        )

    print("Saved model.pkl")


if __name__ == "__main__":
    main()
