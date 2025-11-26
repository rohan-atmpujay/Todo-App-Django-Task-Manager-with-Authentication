from django.db import models
from datetime import date
from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(default=date.today)
    last_date = models.DateField()

    def __str__(self):
        return self.task