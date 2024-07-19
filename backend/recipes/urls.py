from django.urls import path
from .views import get_recipes, add_recipe

urlpatterns = [
    path('recipes/', get_recipes),
    path('recipes/add/', add_recipe),
]
