"""
Compare Random Forest trained on all features vs selected features.
"""

import json
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report


def load_and_prepare_data():
    df = pd.read_csv("../Dataset/output1.csv")
    df = df.drop(columns=["Unnamed: 0", "id"], errors="ignore")

    categorical_cols = df.select_dtypes(include="object").columns.tolist()
    categorical_cols.remove("satisfaction")

    encoders = {}
    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        encoders[col] = le

    X = df.drop("satisfaction", axis=1)
    y = LabelEncoder().fit_transform(df["satisfaction"])

    return X, y


def train_and_evaluate(X, y, feature_names, label):
    X_train, X_test, y_train, y_test = train_test_split(
        X[feature_names], y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=12345)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    acc = accuracy_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_prob)

    print(f"\n{label}")
    print(f"  Features used: {len(feature_names)}")
    print(f"  Feature names: {feature_names}")
    print(f"  Accuracy: {acc:.4f}")
    print(f"  AUC:      {auc:.4f}")

    return {"accuracy": acc, "auc": auc, "model": model}


def main():
    X, y = load_and_prepare_data()
    all_features = list(X.columns)

    with open("../feature_selection_results.json") as f:
        fs_results = json.load(f)

    # Features selected by every method
    method_lists = list(fs_results.values())
    intersection = set(method_lists[0])
    for method_list in method_lists[1:]:
        intersection &= set(method_list)
    intersection_features = sorted(intersection)

    # Features selected by at least 5 out of 7 methods
    from collections import Counter

    all_selected = []
    for method_list in method_lists:
        all_selected.extend(method_list)
    counts = Counter(all_selected)
    frequent_features = [f for f, c in counts.items() if c >= 5]

    print("=" * 60)
    print("Random Forest: all features vs selected features")
    print("=" * 60)

    train_and_evaluate(X, y, all_features, "All features")
    train_and_evaluate(X, y, frequent_features, "Frequently selected features (>=5 methods)")
    train_and_evaluate(X, y, intersection_features, "Intersection of all methods")


if __name__ == "__main__":
    main()
