from django.contrib.auth.models import User
from django.db import models


class Song(models.Model):
    choices = ((0, 'happy'),
               (1, 'angry'),
               (2, 'sad'),
               (3, 'neutral'),
               (4, 'general'))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    track = models.FileField(upload_to='Songs')
    type = models.IntegerField(choices)
    fav=models.BooleanField(default=False)
    name = models.CharField(max_length=30, default="Unknown", blank=True)

    def __str__(self):
        return self.name