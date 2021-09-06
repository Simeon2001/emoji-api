from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class emoji_name (models.Model):
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=20,blank=False)

    def __str__(self):
        return self.name

class emoji_sym (models.Model):
    name = models.ForeignKey(emoji_name,blank=False, on_delete=models.CASCADE, related_name='emoji_names')
    symbol = models.CharField(max_length=2,blank=False)

    def __str__(self):
        return self.symbol