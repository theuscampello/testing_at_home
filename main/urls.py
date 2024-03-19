from django.urls import path
from . import views

urlpatterns = [
    path('', views.studentView, name='student-list'),
    
    
    path('studnetID/<int:id>', views.studentIDview, name='student-list'),

]