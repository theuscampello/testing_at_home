from .models import Student
from django.http import HttpResponse
from django.shortcuts import render


def studentView(request):
    students_list = Student.objects.all()
    return render(request, 'main/students.html', {'students_list': students_list})

# Create your views here.
