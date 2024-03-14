from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Student(models.Model):
    
    name = models.CharField(max_length=254)
    telephone = models.CharField(null = True,blank=True,max_length=15)
    email = models.EmailField()
    date_of_birth = models.DateField()
    #description = models.TextField()
    #updated_at = models.DateTimeField(auto_now=True)
    #user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name