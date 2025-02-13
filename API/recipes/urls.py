from django.urls import path
from .views import RecipeListView, Home, add_recipe, UserListView

urlpatterns = [
    path('', Home, name="Menu"),
    path('recipes/', RecipeListView, name="listar_receitas"),
    path('recipes/new/', add_recipe, name='adicionar receita'),

    path('users/', UserListView, name="listar usuarios")
]