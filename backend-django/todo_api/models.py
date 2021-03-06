from django.db import models
from django.conf import settings
from pytz import timezone
from datetime import datetime


class Todo(models.Model):
    name = models.CharField(max_length=180)
    isCompleted = models.BooleanField(default=False, blank=True)
    createdAt = models.CharField(max_length=180, \
        default=datetime.now(timezone(settings.TIME_ZONE)).strftime("%d/%m/%Y-%H:%M:%S"), \
            blank=True)
    updatedAt = models.CharField(max_length=180, \
        default=datetime.now(timezone(settings.TIME_ZONE)).strftime("%d/%m/%Y-%H:%M:%S"), \
            blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'todo_task'
