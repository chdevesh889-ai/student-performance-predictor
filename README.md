# 🎓 Student Performance Predictor

A machine learning application that predicts a student's exam score based on academic and lifestyle factors using **Linear Regression**.

The project demonstrates an end-to-end machine learning workflow, from data generation and exploratory data analysis to model training, evaluation, model serialization, and deployment through a Streamlit web application.

---

## 📌 Project Overview

The goal of this project is to predict a student's expected exam score using the following factors:

- 📚 Study Hours
- 🏫 Attendance Percentage
- 📝 Previous Marks
- ✅ Assignments Completed
- 😴 Sleep Hours

The project follows this workflow:

**Data Generation → Exploratory Data Analysis → Train/Test Split → Model Training → Evaluation → Model Saving → Prediction Module → Streamlit Application**

---

## 🧠 Machine Learning Approach

### Problem Type

**Supervised Learning → Regression**

The target variable, `exam_score`, is a continuous numerical value, making this a regression problem.

### Algorithm

**Linear Regression**

The model learns the relationship between the input features and the student's exam score.

---

## 📊 Dataset

The dataset contains **500 student records** with:

- **5 input features**
- **1 target variable**

### Features

| Feature | Description |
|---|---|
| `study_hours` | Number of hours spent studying |
| `attendance` | Student attendance percentage |
| `previous_marks` | Marks obtained previously |
| `assignments_completed` | Number of completed assignments |
| `sleep_hours` | Average sleep hours |

### Target

`exam_score` — the student's predicted examination score.

> **Note:** The dataset used in this project is synthetically generated for learning and demonstration purposes. It is not collected from real students.

---

## 🔍 Exploratory Data Analysis

The project uses **Pandas, NumPy, Matplotlib, and Seaborn** for data analysis and visualization.

### Study Hours vs Exam Score

The scatter plot shows the relationship between study hours and exam scores. The dataset shows a positive relationship, where higher study hours generally correspond to higher exam scores.

![Study Hours vs Exam Score](screenshots/study_hours_vs_score.png)

### Feature Correlation Heatmap

The correlation heatmap shows the linear relationship between the numerical features.

In this synthetic dataset, `study_hours` has the strongest correlation with `exam_score`.

![Feature Correlation Heatmap](screenshots/correlation_heatmap.png)

> **Important:** Correlation indicates a statistical relationship; it does not prove causation.

---

## ⚙️ Model Training

The dataset was divided into:

- **80% training data**
- **20% testing data**

A Linear Regression model from **Scikit-learn** was trained using the training dataset.

The trained model was saved using Joblib:

```text
models/student_performance_model.pkl