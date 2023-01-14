
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todos(models.Model):
    task_name=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.task_name