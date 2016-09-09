from django.db import models


# Create your models here.
class Person(models.Model):
    """
    A model for people.
    """
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.URLField(max_length=500)
    skill_one = models.CharField(max_length=255)
    skill_two = models.CharField(max_length=255)
    skill_three = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.name)
