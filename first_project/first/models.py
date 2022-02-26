from django.db import models

STATUS_CHOISES = (
    (1, "new"),
    (2, "doing"),
    (3, "done"),
)


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.status}"
