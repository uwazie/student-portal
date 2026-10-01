from django.contrib import admin
from .models import Result


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):

    list_display = (
        'student',
        'course',
        'ca_score',
        'exam_score',
        'semester',
        'academic_year',
    )

    search_fields = (
        'student__matricule',
        'student__first_name',
        'student__last_name',
        'course__code',
    )

    list_filter = (
        'semester',
        'academic_year',
    )