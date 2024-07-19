from rest_framework.decorators import api_view
from rest_framework.response import Response

recipes = []
next_id = 1

@api_view(['GET'])
def get_recipes(request):
    return Response(recipes)

@api_view(['POST'])
def add_recipe(request):
    global next_id
    global recipes
    recipe = request.data
    recipe['id'] = next_id
    next_id += 1
    recipes.append(recipe)
    return Response(recipe, status=201)

@api_view(['DELETE'])
def delete_recipe(request, id):
    global recipes
    recipe_id = int(id)
    recipe = next((r for r in recipes if r['id'] == recipe_id), None)
    if recipe:
        recipes = [r for r in recipes if r['id'] != recipe_id]
        return Response(status=204)
    return Response({'message': 'Recipe not found'}, status=404)

@api_view(['PUT'])
def update_recipe(request, id):
    global recipes
    recipe_id = int(id)
    updated_recipe = request.data
    for idx, recipe in enumerate(recipes):
        if recipe['id'] == recipe_id:
            recipes[idx] = updated_recipe
            recipes[idx]['id'] = recipe_id
            return Response(updated_recipe, status=200)
    return Response({'message': 'Recipe not found'}, status=404)