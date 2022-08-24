from django.db import models
# from django.contrib.auth import get_user_model
from sysapp.core.models import *



class Client(models.Model):

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    interview_date = models.CharField(max_length=100)
    project_type = models.CharField(max_length=100)
    status = models.BooleanField()
    # import sys 
    # print(sys.path)
    # import pdb; pdb.set_trace()
    # mentor = models.ForeignKey(Mentor, related_name='client', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'