# course_design_app/views.py

from django.shortcuts import render
from django.http import HttpResponse, response
from django.http import JsonResponse
from .models import Course, Term
from io import BytesIO
import reportlab.pdfgen.canvas as canvas
from django.shortcuts import render
from .models import Course, Term

# course_design_app/views.py

def course_design(request):
    terms = Term.objects.all()
    courses = Course.objects.all() 
    if request.method == 'POST':
        # Process GPA calculation when form is submitted
        grades = request.POST.getlist('grade[]')
        credits = request.POST.getlist('credits[]')

        # Your GPA calculation logic here
        # Assume you have a function calculate_gpa(grades, credits) that returns the GPA

        gpa = calculate_gpa(grades, credits)
        return JsonResponse({'gpa': gpa})

    return render(request, 'course_design.html', {'terms': terms, 'courses': courses})

def calculate_gpa(grades, credits):
    # Your GPA calculation logic here
    # You can use a dictionary to map grades to their corresponding GPA values
    grade_points = {'A': 4.0, 'A-': 3.67, 'B+': 3.33, 'B': 3.0, 'B-': 2.67, 'C+': 2.33, 'C': 2.0, 'C-': 1.67, 'D+': 1.33, 'D': 1.0, 'D-': 0.67, 'F': 0.0}

    total_credit_points = 0
    total_credits = 0

    for grade, credit in zip(grades, credits):
        total_credit_points += grade_points.get(grade, 0) * int(credit)
        total_credits += int(credit)

    if total_credits == 0:
        return 0.0
    else:
        return total_credit_points / total_credits
        