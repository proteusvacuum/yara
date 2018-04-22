from django.db import models


class Category(models.Model):
    name = models.TextField()
    slug = models.SlugField()

    class Meta:
        indexes = [
            models.Index(fields=['slug']),
        ]


class Recipe(models.Model):
    last_updated = models.DateField(auto_now=True)

    readable_source = models.TextField()  # the name of the source
    source = models.SlugField()          # A slugified version of the source name

    title = models.TextField()
    link = models.URLField()
    description = models.TextField()
    img = models.URLField()

    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f"<Recipe '{self.readable_source} - {self.title}'>"

    class Meta:
        ordering = ('last_updated', 'source')
        indexes = [
            models.Index(fields=['source']),
        ]
