from django.contrib import admin

# Register your models here.
from .models import Question,Questionset,Category

# @admin.register(Question)
# class QuestionModelAdmin(admin.ModelAdmin):

admin.site.register(Question)
admin.site.register(Questionset)
admin.site.register(Category)
