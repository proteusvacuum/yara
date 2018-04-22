from django.shortcuts import render
from recipes.models import Recipe


def list_recipes(request):
    return render(
        request,
        'recipes/list_recipes.html',
        {
            'recipes': Recipe.objects.all()
        }
    )


home = list_recipes
