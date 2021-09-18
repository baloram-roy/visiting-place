from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='pro_pic')
    address = models.CharField(max_length=255, null=True, blank=True)
    profession = models.CharField(max_length=255, null=True, blank=True)
    hobby = models.CharField(max_length=255, null=True, blank=True)
    biography = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    