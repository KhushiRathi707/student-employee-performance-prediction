from django.shortcuts import render
import pandas as pd
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


# Home Page
def index(request):
    return render(request, "index.html")


# Student Form
def student(request):
    return render(request, "student.html")


# Employee Form
def employee(request):
    return render(request, "employee.html")


# ---------------- STUDENT PREDICTION ----------------

def student_prediction(request):

    age = float(request.GET["age"])
    study_hours = float(request.GET["study_hours"])
    attendance = float(request.GET["attendance"])
    previous_marks = float(request.GET["previous_marks"])
    assignment_score = float(request.GET["assignment_score"])
    quiz_score = float(request.GET["quiz_score"])
    backlogs = float(request.GET["backlogs"])
    activities = float(request.GET["activities"])
    sleep_hours = float(request.GET["sleep_hours"])

    # CSV location
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(BASE_DIR, "student_performance.csv")

    data = pd.read_csv(csv_path)

    features = [
        "Age",
        "StudyHours",
        "Attendance",
        "PreviousMarks",
        "AssignmentScore",
        "QuizScore",
        "Backlogs",
        "Activities",
        "SleepHours"
    ]

    X = data[features]
    y = data["PerformanceScore"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    input_data = [[
        age,
        study_hours,
        attendance,
        previous_marks,
        assignment_score,
        quiz_score,
        backlogs,
        activities,
        sleep_hours
    ]]

    prediction = model.predict(input_data)[0]

    prediction = round(max(0, min(100, prediction)), 2)

    if prediction >= 80:
        level = "Excellent"
        suggestions = [
            "Keep maintaining your current study routine.",
            "Participate in advanced projects and competitions.",
            "Focus on developing practical skills."
        ]

    elif prediction >= 70:
        level = "Good"
        suggestions = [
            "Your performance is good.",
            "Increase practical learning.",
            "Try to improve your weak subjects."
        ]

    elif prediction >= 50:
        level = "Average"
        suggestions = [
            "Increase your daily study hours.",
            "Improve attendance and assignment performance.",
            "Practice more quizzes and coding problems."
        ]

    else:
        level = "Needs Improvement"
        suggestions = [
            "Create a proper daily study schedule.",
            "Focus on attendance and assignments.",
            "Reduce backlogs and improve basic concepts."
        ]

    return render(
        request,
        "result.html",
        {
            "type": "Student",
            "score": prediction,
            "level": level,
            "suggestions": suggestions
        }
    )


# ---------------- EMPLOYEE PREDICTION ----------------

def employee_prediction(request):

    age = float(request.GET["age"])
    experience = float(request.GET["experience"])
    working_hours = float(request.GET["working_hours"])
    projects = float(request.GET["projects"])
    attendance = float(request.GET["attendance"])
    training_hours = float(request.GET["training_hours"])
    previous_performance = float(request.GET["previous_performance"])
    overtime = float(request.GET["overtime"])
    satisfaction = float(request.GET["satisfaction"])
    participation = float(request.GET["participation"])

    # CSV location
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(BASE_DIR, "employee_performance.csv")

    data = pd.read_csv(csv_path)

    features = [
        "Age",
        "Experience",
        "WorkingHours",
        "ProjectsCompleted",
        "Attendance",
        "TrainingHours",
        "PreviousPerformance",
        "OvertimeHours",
        "JobSatisfaction",
        "Participation"
    ]

    X = data[features]
    y = data["PerformanceScore"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    input_data = [[
        age,
        experience,
        working_hours,
        projects,
        attendance,
        training_hours,
        previous_performance,
        overtime,
        satisfaction,
        participation
    ]]

    prediction = model.predict(input_data)[0]

    prediction = round(max(0, min(100, prediction)), 2)

    if prediction >= 80:
        level = "Excellent"
        suggestions = [
            "Excellent employee performance.",
            "Continue taking leadership responsibilities.",
            "Focus on advanced projects."
        ]

    elif prediction >= 70:
        level = "Good"
        suggestions = [
            "Good overall performance.",
            "Improve project contribution.",
            "Continue professional training."
        ]

    elif prediction >= 50:
        level = "Average"
        suggestions = [
            "Improve project involvement.",
            "Attend more training programs.",
            "Focus on productivity and skills."
        ]

    else:
        level = "Needs Improvement"
        suggestions = [
            "Improve work productivity.",
            "Take additional training.",
            "Focus on project participation."
        ]

    return render(
        request,
        "result.html",
        {
            "type": "Employee",
            "score": prediction,
            "level": level,
            "suggestions": suggestions
        }
    )