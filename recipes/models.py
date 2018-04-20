from django.db import models


class Recipe(models.Model):
    title = models.TextField()
    link = models.URLField()
    description = models.TextField()
    img = models.URLField()
