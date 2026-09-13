# 🎓 Student Performance Predictor

A machine learning project that predicts a student's exam score based on academic and lifestyle factors using Linear Regression.

## 📌 Project Overview

The goal of this project is to build an end-to-end machine learning application that predicts a student's expected exam score from:

- Study Hours
- Attendance
- Previous Marks
- Assignments Completed
- Sleep Hours

The project covers the complete ML workflow:

**Data Generation → Data Analysis → Model Training → Evaluation → Model Saving → Prediction → Web Application**

## 🧠 Machine Learning Approach

This is a **Supervised Learning** problem.

### Problem Type

**Regression**

The target variable, `exam_score`, is a continuous numerical value.

### Algorithm

**Linear Regression**

The model learns the relationship between the input features and the student's exam score.

## 📊 Dataset

The dataset contains **500 student records** with 5 input features and 1 target variable.

### Features

| Feature | Description |
|---|---|
| `study_hours` | Number of hours spent studying |
| `attendance` | Student attendance percentage |
| `previous_marks` | Marks obtained previously |
| `assignments_completed` | Number of completed assignments |
| `sleep_hours` | Average sleep hours |

### Target

`exam_score` — predicted examination score.

> **Note:** The dataset used in this project is synthetically generated for learning and demonstration purposes.

## 🔍 Data Analysis

The project includes exploratory data analysis using:

- Pandas
- NumPy
- Matplotlib
- Seaborn

Correlation analysis showed that **study hours had the strongest linear relationship with exam score** among the features in this synthetic dataset.

## 🤖 Model Training

The dataset was divided into:

- **80% training data**
- **20% testing data**

A Linear Regression model was trained using Scikit-learn.

The trained model was then saved as:

```text
models/student_performance_model.pkl