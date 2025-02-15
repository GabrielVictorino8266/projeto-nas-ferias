from django.urls import path
from .views import RecipeListView, Home, Add_recipe, Delete_Recipe, UserListView, Add_user

urlpatterns = [
    path('', Home, name="Menu"),
    path('recipes/', RecipeListView, name="listar_receitas"),
    path('recipes/new/', Add_recipe, name='adicionar receita'),
    path('recipes/delete/<str:id>', Delete_Recipe, name='Delete_Recipe'),

    path('users/', UserListView, name="listar usuarios"),
    path('users/new/', Add_user, name="adicionar usuario")
]
