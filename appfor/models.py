from django.db import models

# Create your models here.

class Room(models.Model):
    #topic =
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    #participants =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    def __str__(self):
        return self.name

