from django.urls import path
from .views import RecipeListView

urlpatterns = [
    path('recipes/', RecipeListView, name="listar_receitas")
]