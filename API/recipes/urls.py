from django.urls import path
from .views import RecipeListView, Home

urlpatterns = [
    path('', Home, name="Menu"),
    path('recipes/', RecipeListView, name="listar_receitas")
]