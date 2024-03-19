from .models import Student
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


def studentView(request):
    students_list = Student.objects.all()
    return render(request, 'main/students.html', {'students_list': students_list})

# Create your views here.
def studentIDview(request, id):
    student = get_object_or_404(Student, pk=id)
    print(student)
    return render(request, 'main/studentID.html', {'student':student})