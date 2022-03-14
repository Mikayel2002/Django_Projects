from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# class Task(models.Model):

STATUS_CHOICE = (
    (0, "New"),
    (1, "Doing"),
    (2, "Done"),
)


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICE, default=0)

    def __str__(self):
        return f"{self.name}-{self.created_at}"
