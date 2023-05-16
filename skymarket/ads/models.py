from django.conf import settings
from django.db import models

from users.models import User


class Ad(models.Model):
    # TODO добавьте поля модели здесь
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=2000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=True)
    image = models.ImageField(upload_to='django_images/', null=True)


class Comment(models.Model):
    # TODO добавьте поля модели здесь
    text = models.CharField(max_length=5000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    created_at = models.DateTimeField()

