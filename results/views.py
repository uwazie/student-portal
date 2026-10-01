from django.shortcuts import render
from .models import Result


def result_list(request):

    results = Result.objects.select_related(
        'student',
        'course'
    ).all()

    return render(
        request,
        'results/result_list.html',
        {
            'results': results
        }
    )