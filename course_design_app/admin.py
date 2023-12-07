# course_design_app/admin.py

from django.contrib import admin
from .models import Course, Term
# course_design_app/admin.py


admin.site.register(Course)
admin.site.register(Term)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_terms')  # Assuming you have a method get_terms in the Course model

    def get_terms(self, obj):
        return ", ".join([term.name for term in obj.terms.all()])
    get_terms.short_description = 'Terms'  # Set a user-friendly name for the column
