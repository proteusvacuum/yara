import hashlib

from django.db import models


class Category(models.Model):
    name = models.TextField()
    slug = models.SlugField()

    class Meta:
        indexes = [
            models.Index(fields=['slug']),
        ]


class RecipeManager(models.Manager):
    def create_recipe(self, *args, **kwargs):
        recipe = self.create(*args, **kwargs)
        return recipe


class Recipe(models.Model):
    objects = RecipeManager()
    last_updated = models.DateField(auto_now=True)

    readable_source = models.TextField()  # the name of the source
    source = models.SlugField()  # A slugified version of the source name
    source_hash = models.CharField(
        max_length=32,
        editable=False,
    )  # A hashed version of the title and source from the spider used for dedup

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
            models.Index(fields=['source_hash']),
        ]


def get_source_hash(title, source):
    return hashlib.md5(f'{title}-{source}'.encode('utf-8')).hexdigest()
