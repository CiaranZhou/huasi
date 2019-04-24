from django.db import models


# Create your models here.
class Interest(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=10)


class Question(models.Model):
    def __str__(self):
        return self.text

    text = models.CharField(max_length=100)
    choice = models.BooleanField()
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)
