from django.db import models
from datetime import date


class Todo(models.Model):
    tittle = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=150, blank=False, null=False)
    date = models.DateField(default=date.today)
    estimated_end = models.DateField(blank=True, null=True)
    priority = models.IntegerField(default=3)

    def __str__(self):
        return self.tittle