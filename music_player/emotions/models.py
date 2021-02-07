from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Prediction(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    emotion = models.CharField(max_length=30)
    image = models.ImageField(upload_to='PredictionImages')
    t_label=models.CharField(max_length=30)
    

    def __str__(self):
        return self.emotion
