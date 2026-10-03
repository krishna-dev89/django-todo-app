from django.db import models
class Todomd(models.Model):
    task=models.CharField(max_length=200)
    completed=models.BooleanField(default=False)
    

# Create your models here.
