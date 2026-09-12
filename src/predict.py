import joblib
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
    student = [[
        study_hours,
        attendance,
        previous_marks,
        assignments_completed,
        sleep_hours
    ]]

    prediction = model.predict(student)

    return prediction[0]