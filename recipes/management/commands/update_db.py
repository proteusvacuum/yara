import json
import os

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from recipes.models import Recipe, get_source_hash


class Command(BaseCommand):
    help = 'Updates the db with new recipes from crawler output'

    def handle(self, *args, **options):
        path = os.path.join(settings.BASE_DIR, 'spiders', 'output')
        created = 0
        skipped = 0

        for filename in os.listdir(path):
            print(f"creating recipes from {filename}")
            with open(os.path.join(path, filename)) as f:
                recipes = json.load(f)
                for recipe in recipes:
                    if add_recipe(recipe):
                        created += 1
                    else:
                        skipped += 1

        print(f"created {created} recipes")
        print(f"skipped {skipped} recipes")


def add_recipe(recipe):
    source_hash = get_source_hash(recipe['title'], recipe['description'])
    try:
        Recipe.objects.get(source_hash=source_hash)
    except Recipe.DoesNotExist:
        recipe['source_hash'] = source_hash
        Recipe.objects.create(**recipe).save()
        return True
    return False
