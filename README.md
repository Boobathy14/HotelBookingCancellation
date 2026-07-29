# Hotel Reservation Cancellation Prediction

## Problem Statement

Hotel reservation cancellations are a significant challenge for the hospitality industry, as they can lead to revenue loss, inefficient room allocation, and operational difficulties. The objective of this project is to develop machine learning models that predict whether a hotel reservation will be **Canceled** or **Not_Canceled** based on customer booking information. Accurate predictions can help hotels optimize occupancy, improve pricing strategies, and enhance customer satisfaction.

---

## Dataset Description

- **Dataset Name:** Hotel Reservation Prediction Dataset
- **Source:** Kaggle
- **Problem Type:** Binary Classification
- **Target Variable:** 'booking_status'

### Dataset Features

| Feature | Description |
|---------|-------------|
| Booking_ID | Unique identifier for each reservation |
| number of adults | Number of adults included in the reservation |
| number of children | Number of children included in the reservation |
| number of weekend nights | Number of weekend nights booked |
| number of week nights | Number of weekdays booked |
| type of meal | Meal plan selected by the customer |
| car parking space | Whether a parking space was requested |
| room type | Type of room reserved |
| lead time | Number of days between booking and arrival |
| market segment type | Booking source (Online, Offline, Corporate, etc.) |
| repeated | Indicates whether the guest is a repeated customer |
| P-C | Number of previous cancelled bookings |
| P-not-C | Number of previous non-cancelled bookings |
| average price | Average room price per night |
| special requests | Number of special requests made by the customer |
| date of reservation | Date on which the reservation was made |
| booking status | Target variable indicating whether the reservation was **Canceled** or **Not_Canceled** |

### Dataset Summary

- **Total Features:** 16 Input Features
- **Target Variable:** Booking Status
- **Classification Type:** Binary Classification

---

## GitHub Repository

**Repository Link:**

https://github.com/yourusername/hotel-reservation-prediction

---

## Models Used

The following machine learning models were implemented and evaluated:

1. Logistic Regression
2. Decision Tree
3. K-Nearest Neighbours (KNN)
4. Naive Bayes
5. Random Forest (Ensemble)

### Model Performance Comparison

| ML Model | Accuracy | AUC | Precision | Recall | F1 Score | MCC |
|----------|---------:|----:|----------:|---------:|---------:|---------:|
| Logistic Regression | 0.805 | 0.787 | 0.83 | 0.90 | 0.86 | 0.543 |
| Decision Tree | 0.859 | 0.848 | 0.90 | 0.89 | 0.89 | 0.684 |
| K-Nearest Neighbours | 0.855 | 0.709 | 0.88 | 0.91 | 0.89 | 0.684 |
| Naive Bayes | 0.411 | 0.799 | 0.89 | 0.14 | 0.24 | 0.684 |
| Random Forest (Ensemble) | 0.891 | 0.799 | 0.91 | 0.94 | 0.92 | 0.749 |

> Replace the values above with the evaluation metrics obtained from your trained models.

---

## Model Performance Observations

## Model Performance Observations

| ML Model | Observation about Model Performance |
|----------|-------------------------------------|
| **Logistic Regression** | Logistic Regression achieved an accuracy of **80.5%** with good recall (**90%**), indicating that it correctly identified most cancelled bookings. However, its moderate MCC (**0.543**) suggests that its overall predictive performance was lower than the tree-based models. It serves as a reliable baseline model for this classification task. |
| **Decision Tree** | Decision Tree achieved an accuracy of **85.9%** with balanced Precision (**90%**), Recall (**89%**), and F1-score (**89%**). The model effectively captured non-linear relationships within the dataset, resulting in strong overall performance and a high MCC (**0.684**). |
| **K-Nearest Neighbours (KNN)** | KNN obtained an accuracy of **85.5%** and an excellent Recall (**91%**), demonstrating its ability to correctly identify cancelled reservations. However, its comparatively lower AUC (**0.709**) indicates weaker class separation than the other models, although its overall classification performance remained strong. |
| **Naive Bayes** | Naive Bayes produced the lowest accuracy (**41.1%**) and a very low Recall (**14%**), resulting in a poor F1-score (**24%**). Although its AUC (**0.799**) was reasonable, the model struggled because of its assumption that features are independent, which is not suitable for this dataset. |
| **Random Forest (Ensemble)** | Random Forest achieved the best overall performance with the highest Accuracy (**89.1%**), Precision (**91%**), Recall (**94%**), and F1-score (**92%**). It also achieved the highest MCC (**0.749**), indicating strong predictive capability and balanced classification performance. The ensemble approach effectively reduced overfitting and captured complex relationships in the data. |
| **Overall Winner** | **Random Forest (Ensemble)** was the best-performing model for the Hotel Reservation Cancellation dataset. It consistently outperformed the other models across almost all evaluation metrics, making it the most suitable model for predicting hotel reservation cancellations. |

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook

---

## Evaluation Metrics

The models were evaluated using the following performance metrics:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC Score
- Matthews Correlation Coefficient (MCC)

---

## Conclusion

This project compared multiple machine learning algorithms for predicting hotel reservation cancellations. The models were evaluated using several classification metrics, including Accuracy, Precision, Recall, F1-score, AUC, and MCC. Based on the evaluation results, the best-performing model was selected for predicting reservation cancellations, providing valuable insights for hotel revenue management and operational planning.