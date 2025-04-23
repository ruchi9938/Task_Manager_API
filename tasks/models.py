from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name