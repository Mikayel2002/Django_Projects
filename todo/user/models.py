from django.contrib.auth.models import User
from django.db import models
from dateutil.relativedelta import relativedelta
from django.utils import timezone
from django.core.mail import send_mail

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_birth = models.DateTimeField()
    field = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(default='static/user/images/default_profile.jpg', upload_to='profile_images', null=True, blank=True)

    def age(self):
        return relativedelta(timezone.now().date(), self.date_birth).years

    def save(self, *args, **kwargs):
        data = super().save(*args, **kwargs)

        # TODO send email
        send_mail(
            subject="Profile",
            message="We have created a profile for you",
            from_email="mikayelmurad@gmail.com",
            recipient_list=[self.user.email]
        )

        return data

    def __str__(self):
        return f"{self.user.username}"
