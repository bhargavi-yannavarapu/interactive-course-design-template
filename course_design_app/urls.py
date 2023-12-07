from django.urls import path
from .views import course_design, calculate_gpa

urlpatterns = [
    path('', course_design, name='course_design'),
    path('semester/<int:semester_id>/', calculate_gpa, name='gpa_calculator'),
    # Add other paths as needed
]

