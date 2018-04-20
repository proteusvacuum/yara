from django.shortcuts import render


def list_recipes(request):
    return render(request, 'recipes/list_recipes.html')
