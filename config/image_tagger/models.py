from django.db import models
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager

from django.conf import settings


class Image(models.Model):
    title = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/")
    submitter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tags = TaggableManager()

    def __str__(self):
        return self.title
