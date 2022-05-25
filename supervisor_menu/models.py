from django.db import models


def add_ten(model):
    largest = model.objects.all().largest


class SupervisorMenuItem(models.Model):

    text = models.CharField(max_length=20, help_text='Menu Item Text')
    url = models.CharField(max_length=40)
    ordering = models.IntegerField(default=1)

    def add_ten(self):
        largest = self.objects.all().largest

    def __str__(self):
        return self.text


class SupervisorSubMenuItem(models.Model):
    text = models.CharField(max_length=20, help_text='Sub menu item text')
    url = models.CharField(max_length=40)
    ordering = models.IntegerField()
    parent = models.ForeignKey('SupervisorMenuItem',
                               blank=True, null=True,
                               related_name='children',
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.text

