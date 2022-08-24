from django.db import models
from django.contrib.auth.models import AbstractUser
# from config import settings
from sysapp.client.models import *


STATE_CHOICE=((
    ('Python','Python'),
    ('Java','Java'),
    ('React','React'),
    ('Angular','Angular'),
    ('Node','Node'),
    ('PHP','PHP'),


))

class User (AbstractUser):
    mobile = models.CharField(max_length=25, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    client = models.ForeignKey(Client, related_name='user',on_delete=models.CASCADE)
    type = models.CharField(choices=STATE_CHOICE, max_length=50)

    def __str__(self):
        return f"{self.first_name}/{self.email}"


class Mentor(models.Model):
    name = models.CharField(max_length=100)
    assigned_date = models.DateField(auto_now=False, auto_now_add=False)
    status = models.BooleanField()

    def __str__(self):
        return f'{self.name}'

# class Client(models.Model):

#     name = models.CharField(max_length=100)
#     address = models.CharField(max_length=100)
#     interview_date = models.CharField(max_length=100)
#     project_type = models.CharField(max_length=100)
#     status = models.BooleanField()
#     mentor = models.ForeignKey(Mentor, related_name='client', on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.name}'
