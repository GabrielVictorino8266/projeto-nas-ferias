from django.urls import path
from .views import RecipeListView, Home, add_recipe

urlpatterns = [
    path('', Home, name="Menu"),
    path('recipes/', RecipeListView, name="listar_receitas"),
    path('recipes/new/', add_recipe, name='adicionar receita')
]