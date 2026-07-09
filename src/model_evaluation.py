"""
Model Evaluation
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ### <b>Objective</b>
# - <b><font color='yellow'>Can we accurately predict when our airline customer will churn or will not?</font></b> **--------->** <b><font color='yellow'>can we build a model to do so?</font></b> **----------->** <b><font color='yellow'>what sort of features are we going to have to include in the model?</font></b>
#




# <h5>Whether a customer is satisfied or dissatisfied, can we find the factors/features that push them to be so?</h5>
#
# Update: still no exact answer to the above question....




# ### Comparison between all models(not including unregularized) in one go!!!!

import matplotlib.pyplot as plt
import scikitplot as skplt
from sklearn.metrics import roc_auc_score

def compare_models(models, X_test, y_test):
    model_names = []
    auc_scores = []

    for i, model in enumerate(models):
        model_name = f"Model {i+1}"
        model_names.append(model_name)

        # Make predictions
        y_pred_prob = model.predict_proba(X_test)[:, 1]

        # Calculate AUC score
        auc = roc_auc_score(y_test, y_pred_prob)
        auc_scores.append(auc)

        # Plot ROC curve
        skplt.metrics.plot_roc(y_test, model.predict_proba(X_test), title=f"ROC Curve - {model_name}")

    # Plot AUC comparison
    plt.figure(figsize=(10, 6))
    plt.bar(model_names, auc_scores)
    plt.xlabel("Model")
    plt.ylabel("AUC Score")
    plt.title("AUC Comparison")
    plt.show()

    # Print AUC scores
    for model_name, auc_score in zip(model_names, auc_scores):
        print(f"{model_name}: AUC = {auc_score}")


# Define the models
models = [
    model_1,
    model_2,
    model_3,
    model_lr,
    model_5,
    model_rf
]


M_unregularized


# Call the function to compare models
compare_models(models, X_test, y_test)





# ## <center>**Conclusion**</center>




