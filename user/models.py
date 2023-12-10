from django.db import models
from datetime import date

class user_info(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    added_date = models.DateField(default=date.today())

    def __str__(self):
        return f"{self.name}"
