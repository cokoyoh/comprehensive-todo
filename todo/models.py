from django.db import models
from django.utils import timezone


class Todo(models.Model):
    task = models.TextField()
    date = models.DateField()
    completed_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(default=timezone.now().strftime("%Y-%m-%d %H:%M:%S"))
    updated_at = models.DateTimeField(default=timezone.now().strftime("%Y-%m-%d %H:%M:%S"))

    class Meta:
        db_table = 'todos'
        ordering = ['-created_at']

    def __str__(self):
        return self.task