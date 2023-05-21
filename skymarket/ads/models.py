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

    @property
    def author_first_name(self):
        return self.author.first_name if self.author else None

    @property
    def author_last_name(self):
        return self.author.last_name if self.author else None

    @property
    def phone(self):
        return self.author.phone if self.author else None


class Comment(models.Model):
    # TODO добавьте поля модели здесь
    text = models.CharField(max_length=5000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=True)

    @property
    def author_first_name(self):
        return self.author.first_name if self.author else None

    @property
    def author_last_name(self):
        return self.author.last_name if self.author else None

    @property
    def author_image(self):
        return self.author.image if self.author.image else None

