# from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .mongodb import get_all_recipes

def RecipeListView(request):
    # Obter todas as receitas
    recipes = get_all_recipes()
    
    # Retornar as receitas como uma resposta JSON
    return JsonResponse({"recipes": recipes})


def Home(request):
    return HttpResponse('Para acessar o endpoint: /recipes')
