from django.urls import path
from . import views

urlpatterns = [

    path("", views.index, name="index"),

    path("student/", views.student, name="student"),

    path(
        "student/predict/",
        views.student_prediction,
        name="student_prediction"
    ),

    path("employee/", views.employee, name="employee"),

    path(
        "employee/predict/",
        views.employee_prediction,
        name="employee_prediction"
    ),
]