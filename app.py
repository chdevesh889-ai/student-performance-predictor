import streamlit as st
from src.predict import predict_exam_score


st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)


st.title("🎓 Student Performance Predictor")

st.write(
    "Enter the student's academic and lifestyle information "
    "to predict their exam score."
)


st.subheader("Student Information")


study_hours = st.number_input(
    "Study Hours",
    min_value=0.0,
    max_value=24.0,
    value=5.0,
    step=0.5
)


attendance = st.number_input(
    "Attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value=75.0,
    step=1.0
)


previous_marks = st.number_input(
    "Previous Marks",
    min_value=0.0,
    max_value=100.0,
    value=70.0,
    step=1.0
)


assignments_completed = st.number_input(
    "Assignments Completed",
    min_value=0,
    max_value=10,
    value=7,
    step=1
)


sleep_hours = st.number_input(
    "Sleep Hours",
    min_value=0.0,
    max_value=24.0,
    value=7.0,
    step=0.5
)


if st.button("Predict Exam Score"):

    prediction = predict_exam_score(
        study_hours,
        attendance,
        previous_marks,
        assignments_completed,
        sleep_hours
    )

    st.success(f"Predicted Exam Score: {prediction:.2f}")