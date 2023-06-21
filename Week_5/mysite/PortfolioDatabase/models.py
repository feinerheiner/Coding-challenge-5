from django.db import models


# Create your models here.
class Hobby(models.Model):
    def __str__(self):
        return self.hobby_name

    hobby_name = models.CharField(max_length=200)
    hobby_desc = models.CharField(max_length=400)


class Project(models.Model):
    def __str__(self):
        return self.project_name

    project_name = models.CharField(max_length=200)
    project_desc = models.CharField(max_length=400)

