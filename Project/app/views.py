from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .models import Course
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    courses = Course.objects.all()
    return render(request, 'app/main.html', {'courses': courses})

def detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'app/detail.html', {'course': course})

def rate(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        new_rating = float(request.POST.get('rating'))
        course.rate = (course.rate * course.count + new_rating) / (course.count + 1)
        course.count += 1
        course.save()
        return redirect('detail', course_id=course.id)
    return render(request, 'app/rate.html', {'course': course})
