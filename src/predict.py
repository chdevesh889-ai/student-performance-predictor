import joblib
import pandas as pd
from pathlib import Path


# Load the trained model
model_path = (
    Path(__file__).resolve().parent.parent
    / "models"
    / "student_performance_model.pkl"
)

model = joblib.load(model_path)


def predict_exam_score(
    study_hours,
    attendance,
    previous_marks,
    assignments_completed,
    sleep_hours
):
    student = pd.DataFrame([{
        "study_hours": study_hours,
        "attendance": attendance,
        "previous_marks": previous_marks,
        "assignments_completed": assignments_completed,
        "sleep_hours": sleep_hours
    }])

    prediction = model.predict(student)

    return prediction[0]