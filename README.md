# Airline Customer Satisfaction Prediction

A Streamlit app that predicts airline passenger satisfaction and explores the key drivers behind it.

**Live demo:** https://airline-satisfaction-seth.streamlit.app

---

## What it does

- **Predicts satisfaction** from flight experience ratings using a Random Forest model.
- **Explores the data** with interactive visualizations.
- **Compares feature-selection methods** and shows which features matter most.
- **Benchmarks multiple ML models** (Random Forest, Decision Tree, Logistic Regression variants, Elastic Net).

Built on roughly **130,000 airline records** and **22 input features** covering demographics, flight info, and inflight service ratings.

---

## Tech stack

- Python 3.10+ / 3.14
- Streamlit
- scikit-learn
- pandas
- matplotlib / seaborn

---

## Project structure

```
.
├── app.py                          # Streamlit app entry point
├── train_model.py                  # Script to retrain and save model.pkl
├── requirements.txt                # Python dependencies
├── model.pkl                       # Trained Random Forest + encoders (84 MB)
├── feature_selection_results.json  # Feature selection outputs
├── feature_comparison_results.json
├── Dataset/
│   └── output1.csv                 # Cleaned dataset used by the app
├── src/                            # Modular pipeline scripts
│   ├── data_cleaning.py
│   ├── eda.py
│   ├── feature_selection.py
│   ├── model_training.py
│   └── model_evaluation.py
└── notebooks/                      # Jupyter notebooks for each stage
    ├── 01_data_cleaning.ipynb
    ├── 02_eda.ipynb
    ├── 03_feature_selection.ipynb
    ├── 04_model_training.ipynb
    └── 05_model_evaluation.ipynb
```

---

## Run locally

```bash
# 1. Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501`.

### Retrain the model

```bash
python train_model.py
```

This reads `Dataset/output1.csv`, trains a Random Forest, and writes a new `model.pkl`.

---

## Deploy to Streamlit Community Cloud

1. Push the repo to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in.
3. Click **Create app**.
4. Select:
   - **Repository:** your GitHub repo
   - **Branch:** the branch containing the app
   - **Main file path:** `app.py`
5. Click **Deploy**.

> **Note:** As of mid-2026, Streamlit Community Cloud defaults to Python 3.14 and ignores `runtime.txt`. This repo uses package versions compatible with Python 3.14 (`scikit-learn==1.7.2`, `pandas==2.3.3`, etc.) so deployment works without needing to pin an older Python version.

---

## Model performance

| Model                   | AUC   |
| ----------------------- | ----- |
| Random Forest           | 0.994 |
| Decision Tree           | 0.946 |
| Lasso Logistic Reg.     | 0.927 |
| Ridge Logistic Reg.     | 0.908 |
| Plain Logistic Reg.     | 0.751 |
| Elastic Net             | 0.641 |

The deployed predictor uses the **Random Forest** trained on all available features.

---

## Key drivers of satisfaction

- Type of Travel
- Inflight Wi-Fi Service
- Online Boarding
- Seat Comfort
- Class

---

## Author

pisethTang
