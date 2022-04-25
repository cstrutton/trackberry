from django.db import models
from django.urls import reverse


class SupervisorMenuItem(models.Model):

    text = models.CharField(max_length=20, help_text='Menu Item Text')
    url = models.CharField(max_length=40)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.text
