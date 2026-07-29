import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
)

st.title("Hotel Reservation Cancellation Prediction")

# Upload dataset
uploaded_file = st.file_uploader(
    "Upload Test Dataset (CSV)",
    type=["csv"]
)

# Select model
model_name = st.selectbox(
    "Choose Model",
    [
        "Logistic Regression",
        "Decision Tree",
        "KNN",
        "Naive Bayes",
        "Random Forest"
    ]
)

# Load selected model
if model_name == "Logistic Regression":
    model = joblib.load("models/logistic.pkl")

elif model_name == "Decision Tree":
    model = joblib.load("models/decision_tree.pkl")

elif model_name == "KNN":
    model = joblib.load("models/knn.pkl")

elif model_name == "Naive Bayes":
    model = joblib.load("models/naive_bayes.pkl")

else:
    model = joblib.load("models/random_forest.pkl")

# Run only after file upload
if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Dataset")
    st.dataframe(df.head())

    # Split features and target
    X = df.drop(['booking status','Booking_ID', 'date of reservation'], axis=1)
    y = df['booking status']

    le = LabelEncoder()
    
    y = le.fit_transform(df["booking status"])

    X = pd.get_dummies(X, drop_first=True)

    # Prediction
    y_pred = model.predict(X)

    le = LabelEncoder()

    y = le.fit_transform(df["booking status"])

    st.subheader("Evaluation Metrics")

    st.write("Accuracy:", accuracy_score(y, y_pred))
    st.write("Precision:", precision_score(y, y_pred, average="binary"))
    st.write("Recall:", recall_score(y, y_pred, average="binary"))
    st.write("F1 Score:", f1_score(y, y_pred, average="binary"))

    st.subheader("Classification Report")
    st.text(classification_report(y, y_pred))

    st.subheader("Confusion Matrix")

    cm = confusion_matrix(y, y_pred)

    fig, ax = plt.subplots(figsize=(5, 4))

    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        ax=ax
    )

    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")

    st.pyplot(fig)

else:
    st.info("Please upload a CSV file to continue.")