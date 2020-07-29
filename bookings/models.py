from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , blank=True)
    feedback = models.TextField()

    def __str__(self):
        return self.user.username
