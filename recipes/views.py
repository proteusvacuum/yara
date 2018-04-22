from django.shortcuts import render
from recipes.models import Recipe


def _list_recipes(request, recipes):
    return render(
        request,
        'recipes/list_recipes.html',
        {
            'recipes': recipes
        }
    )

def list_all_recipes(request):
    return _list_recipes(request, Recipe.objects.all())

home = list_all_recipes


def list_recipes_by_source(request, source):
    """lists all recipes from a particular source
    """
    return _list_recipes(request, Recipe.objects.filter(source=source))


def list_recipes_by_category(request, category):
    """lists all recipes from a particular source
    """
    return _list_recipes(request, Recipe.objects.filter(categories__slug=category))
