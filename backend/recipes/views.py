from rest_framework.decorators import api_view
from rest_framework.response import Response

recipes = []

@api_view(['GET'])
def get_recipes(request):
    return Response(recipes)

@api_view(['POST'])
def add_recipe(request):
    recipe = request.data
    recipes.append(recipe)
    return Response(recipe, status=201)
