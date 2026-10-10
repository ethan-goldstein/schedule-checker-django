from django.shortcuts import get_object_or_404, redirect, render

from .forms import CourseForm
from .models import Course

MAX_CREDITS = 18


def schedule(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule')
    else:
        form = CourseForm()

    courses = list(Course.objects.order_by('start_time'))

    # check every pair of classes once
    conflicts = []
    for i, first in enumerate(courses):
        for second in courses[i + 1:]:
            if first.conflicts_with(second):
                conflicts.append((first, second))

    total_credits = sum(course.credits for course in courses)

    return render(request, 'planner/schedule.html', {
        'form': form,
        'courses': courses,
        'conflicts': conflicts,
        'total_credits': total_credits,
        'over_limit': total_credits > MAX_CREDITS,
        'max_credits': MAX_CREDITS,
    })


def delete_course(request, pk):
    if request.method == 'POST':
        get_object_or_404(Course, pk=pk).delete()
    return redirect('schedule')