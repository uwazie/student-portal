from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'matricule',
        'first_name',
        'last_name',
        'programme',
        'level',
        'email',
    )

    search_fields = (
        'matricule',
        'first_name',
        'last_name',
        'email',
    )

    list_filter = (
        'programme',
        'level',
    )