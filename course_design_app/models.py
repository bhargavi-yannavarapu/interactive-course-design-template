from django.db import models
from django.contrib.auth.models import User

from django.db import models

class Term(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=50)
    term = models.ForeignKey(Term, on_delete=models.CASCADE, default=1)
    grade = models.CharField(max_length=2, blank=True, null=True)  # New field for storing grades

    def __str__(self):
        return self.name

   
