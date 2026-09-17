import pandas as pd
import random


# ==============================
# STUDENT DATASET
# ==============================

student_data = []

for i in range(500):

    age = random.randint(18, 25)
    study_hours = round(random.uniform(1, 10), 1)
    attendance = round(random.uniform(50, 100), 1)
    previous_marks = round(random.uniform(40, 95), 1)
    assignment_score = round(random.uniform(40, 100), 1)
    quiz_score = round(random.uniform(40, 100), 1)
    backlogs = random.randint(0, 5)
    activities = random.randint(0, 10)
    sleep_hours = round(random.uniform(4, 9), 1)

    score = (
        study_hours * 4
        + attendance * 0.20
        + previous_marks * 0.25
        + assignment_score * 0.10
        + quiz_score * 0.10
        + activities * 0.5
        
        - backlogs * 4
        + sleep_hours * 1
    )

    score = max(0, min(100, score))

    student_data.append([
        age,
        study_hours,
        attendance,
        previous_marks,
        assignment_score,
        quiz_score,
        backlogs,
        activities,
        sleep_hours,
        round(score, 2)
    ])


student_columns = [
    "Age",
    "StudyHours",
    "Attendance",
    "PreviousMarks",
    "AssignmentScore",
    "QuizScore",
    "Backlogs",
    "Activities",
    "SleepHours",
    "PerformanceScore"
]

student_df = pd.DataFrame(
    student_data,
    columns=student_columns
)

student_df.to_csv(
    "student_performance.csv",
    index=False
)


# ==============================
# EMPLOYEE DATASET
# ==============================

employee_data = []

for i in range(500):

    age = random.randint(21, 55)
    experience = round(random.uniform(0, 20), 1)
    working_hours = round(random.uniform(6, 12), 1)
    projects = random.randint(0, 20)
    attendance = round(random.uniform(60, 100), 1)
    training_hours = round(random.uniform(0, 50), 1)
    previous_performance = round(random.uniform(40, 100), 1)
    overtime = round(random.uniform(0, 30), 1)
    satisfaction = random.randint(1, 10)
    participation = random.randint(1, 10)

    score = (
        experience * 1.5
        + projects * 2
        + attendance * 0.20
        + training_hours * 0.20
        + previous_performance * 0.35
        + satisfaction * 1.5
        + participation * 1.2
        - overtime * 0.5
    )

    score = max(0, min(100, score))

    employee_data.append([
        age,
        experience,
        working_hours,
        projects,
        attendance,
        training_hours,
        previous_performance,
        overtime,
        satisfaction,
        participation,
        round(score, 2)
    ])


employee_columns = [
    "Age",
    "Experience",
    "WorkingHours",
    "ProjectsCompleted",
    "Attendance",
    "TrainingHours",
    "PreviousPerformance",
    "OvertimeHours",
    "JobSatisfaction",
    "Participation",
    "PerformanceScore"
]

employee_df = pd.DataFrame(
    employee_data,
    columns=employee_columns
)

employee_df.to_csv(
    "employee_performance.csv",
    index=False
)


print("Student dataset created successfully!")
print("Employee dataset created successfully!")