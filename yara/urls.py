"""yara URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from recipes.views import (
    home,
    list_all_recipes,
    list_recipes_by_category,
    list_recipes_by_source,
    search,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('recipes', list_all_recipes, name='list_all_recipes'),
    path('recipes/source/<slug:source>/', list_recipes_by_source, name='list_recipes_by_source'),
    path('recipes/category/<slug:category>/', list_recipes_by_category, name='list_recipes_by_category'),
    path('recipes/search/', search, name='search'),
]
