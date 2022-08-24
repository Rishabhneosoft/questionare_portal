from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=200)
    # import pdb; pdb.set_trace()
    category_type = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.question

class Questionset(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)

    def __str__(self):
        return self.question

class Category(models.Model):
    name = models.CharField(max_length=100)
    category_type = models.ChoiceField()

    def __str__(self):
        return self.name