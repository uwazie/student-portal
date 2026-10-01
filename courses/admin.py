from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = (
        'code',
        'title',
        'programme',
        'level',
        'semester',
        'credits',
    )

    search_fields = (
        'code',
        'title',
    )

    list_filter = (
        'programme',
        'level',
        'semester',
    )