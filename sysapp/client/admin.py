from django.contrib import admin
from .models import Client
# Register your models here.
admin.site.register(Client)

# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['id', 'stuname', 'email']