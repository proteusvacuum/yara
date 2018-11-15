from django.shortcuts import render
from recipes.models import Recipe

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

client = Elasticsearch()


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


def search(request):
    q = request.GET.get('q', '*')
    search_results = (
        Search(using=client, index='recipes')
        .filter("term", title=q)
        .source(exclude=["@timestamp", "@version"])
    )
    recipes = [Recipe(**r.to_dict()) for r in search_results]
    return _list_recipes(request, recipes)
