from django.shortcuts import render

from students.models import Student
from courses.models import Course
from results.models import Result


def home(request):
    return render(request, 'home.html')


def dashboard(request):

    total_students = Student.objects.count()
    total_courses = Course.objects.count()
    total_results = Result.objects.count()

    context = {
        'total_students': total_students,
        'total_courses': total_courses,
        'total_results': total_results,
    }

    return render(
        request,
        'dashboard.html',
        context
    )