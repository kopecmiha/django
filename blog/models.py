from django.conf import settings
from django.db import models
from django.utils import timezone
import uuid


class Message(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now())
    title = models.TextField()

    def create(self, user, time, title):
        self.user = user
        self.time = time
        self.title = title
        self.save()

    def __repr__(self):
        return str({"user": self.user, "time": self.time, "title": self.title})


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.TextField()

    def create(self, id, username):
        self.id = id
        self.username = username
        self.save()

    def __repr__(self):
        return str({"id": self.id, "username": self.username})
