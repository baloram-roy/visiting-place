from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name

class Place(models.Model):
    DHAKA = 'D'
    CHITAGONG = 'C'
    RAJSHAHI = 'R'
    KHULNA = 'K'
    BARISHAL = 'B' 
    SHYLET = 'S'

    DIVISION_CHOICES = [
        (DHAKA,'Dhaka'),
        (CHITAGONG,'Chitagong'),
        (RAJSHAHI,'Rajshahi'),
        (KHULNA,'Khulna'),
        (BARISHAL,'Barishal'),
        (SHYLET,'Shylet'),
    ]

    image = models.ImageField(default='default.jpg', upload_to='place')
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=50)
    division = models.CharField(
        max_length=20,
        choices=DIVISION_CHOICES,
        default=DHAKA
        )
    description = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
        )
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('place-detail', kwargs={'pk': self.pk})