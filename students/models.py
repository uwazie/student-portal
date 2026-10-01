from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):

    LEVEL_CHOICES = [
        ('100', 'Level 100'),
        ('200', 'Level 200'),
        ('300', 'Level 300'),
        ('400', 'Level 400'),
        ('500', 'Level 500'),
    ]



    matricule = models.CharField(
        max_length=20,
        unique=True
    )

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    programme = models.CharField(
        max_length=150
    )

    level = models.CharField(
        max_length=3,
        choices=LEVEL_CHOICES
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    address = models.TextField(
        blank=True
    )

    photo = models.ImageField(
        upload_to='students/',
        blank=True,
        null=True
    )

    date_registered = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.matricule} - {self.first_name} {self.last_name}"

    class Meta:
        ordering = ['last_name', 'first_name']