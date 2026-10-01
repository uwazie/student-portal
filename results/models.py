from django.db import models
from students.models import Student
from courses.models import Course


class Result(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='results'
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='results'
    )

    ca_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )

    exam_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )

    semester = models.CharField(
        max_length=20
    )

    academic_year = models.CharField(
        max_length=20
    )

    @property
    def total_score(self):
        return self.ca_score + self.exam_score

    @property
    def grade(self):
        total = self.total_score

        if total >= 80:
            return 'A'
        elif total >= 70:
            return 'B'
        elif total >= 60:
            return 'C'
        elif total >= 50:
            return 'D'
        elif total >= 40:
            return 'E'
        return 'F'

    def __str__(self):
        return f"{self.student} - {self.course}"