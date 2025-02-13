from django.urls import path
from .views import RecipeListView, Home, Add_recipe, UserListView, Add_user

urlpatterns = [
    path('', Home, name="Menu"),
    path('recipes/', RecipeListView, name="listar_receitas"),
    path('recipes/new/', Add_recipe, name='adicionar receita'),

    path('users/', UserListView, name="listar usuarios"),
    path('users/new/', Add_user, name="adicionar usuario")
]