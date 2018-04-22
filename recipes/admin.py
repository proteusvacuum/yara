from django.contrib import admin

from recipes.models import Category, Recipe


class RecipeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Recipe, RecipeAdmin)


class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
