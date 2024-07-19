from django.urls import path
from .views import get_recipes, add_recipe, delete_recipe, update_recipe

urlpatterns = [
    path('recipes/', get_recipes),
    path('recipes/add/', add_recipe),
    path('recipes/delete/<int:id>/', delete_recipe),
    path('recipes/edit/<int:id>/', update_recipe),
]