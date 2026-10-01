from django.db import models


class Course(models.Model):

    code = models.CharField(
        max_length=20,
        unique=True
    )

    title = models.CharField(
        max_length=200
    )

    credits = models.PositiveIntegerField(
        default=3
    )

    programme = models.CharField(
        max_length=150
    )

    level = models.CharField(
        max_length=20
    )

    semester = models.CharField(
        max_length=20
    )

    lecturer = models.CharField(
        max_length=150,
        blank=True
    )

    def __str__(self):
        return f"{self.code} - {self.title}"

    class Meta:
        ordering = ['code']