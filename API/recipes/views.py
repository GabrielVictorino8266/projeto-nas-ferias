from django.http import JsonResponse, HttpResponse
from .mongodb import get_all_recipes, save_recipe, get_all_users, save_user
import json
from datetime import datetime, timezone
from .validations import validate_recipe_data, validate_user_data


def RecipeListView(request):
    # Obter todas as receitas
    if request.method == "GET":
        recipes = get_all_recipes()
        # Retornar as receitas como uma resposta JSON
        return JsonResponse({"recipes": recipes})
    else:
        return JsonResponse({"error": "Método não permitido"}, status=405)


def Home(request):
    return HttpResponse('Para acessar o endpoint: /recipes')


def Add_recipe(request):
    if request.method == "POST":
        try:
            # Carregar os dados JSON
            data = json.loads(request.body)

            # Obter os campos do corpo da requisição
            title = data.get("title")
            description = data.get("description")
            ingredients = data.get("ingredients")
            instructions = data.get("instructions")
            ratings = data.get("ratings", [])  # Se não houver ratings, será uma lista vazia

            # Validar os dados
            validate_recipe_data(title, description, ingredients, instructions, ratings)

            # Validar e ajustar a data de criação
            creation_date = data.get("creation_date", {}).get("$date")
            if creation_date:
                try:
                    creation_date = datetime.strptime(creation_date, "%Y-%m-%dT%H:%M:%S.%fZ")
                except ValueError:
                    return JsonResponse({"error": "Formato de data inválido"}, status=400)
            else:
                creation_date = datetime.now(timezone.utc).isoformat()

            #recipe_id = save_recipe(title, description, ingredients, instructions, creation_date, ratings)
            recipe_id = 0000000000

            return JsonResponse({"message": "Receita adicionada!", "id": str(recipe_id)}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido"}, status=400)

        except ValueError as e:
            # Captura de erro de validação (como erro no tipo de dado)
            return JsonResponse({"error": str(e)}, status=400)

    # Caso o método não seja POST
    return JsonResponse({"error": "Método não permitido"}, status=405)


def UserListView(request):
    # Obter todos usuários
    if request.method == "GET":
        users = get_all_users()
        # Retornar as receitas como uma resposta JSON
        return JsonResponse({"users": users})
    else:
        return JsonResponse({"error": "Método não permitido"}, status=405)
    

def Add_user(request):
    if request.method == "POST":
        try:
            # Carregar os dados JSON
            data = json.loads(request.body)

            # Obter os campos do corpo da requisição
            name = data.get("name")
            email = data.get("email")
            password = data.get("password")

            # Validar os dados
            validate_user_data(name, email, password)

            # Validar e ajustar a data de criação
            creation_date = data.get("creation_date", {}).get("$date")
            if creation_date:
                try:
                    creation_date = datetime.strptime(creation_date, "%Y-%m-%dT%H:%M:%S.%fZ")
                except ValueError:
                    return JsonResponse({"error": "Formato de data inválido"}, status=400)
            else:
                creation_date = datetime.now(timezone.utc).isoformat()

            #user_id = save_user(name, email, password, creation_date)
            user_id = 11111111111
            return JsonResponse({"message": "Usuário adicionado!", "id": str(user_id)}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido"}, status=400)

        except ValueError as e:
            # Captura de erro de validação (como erro no tipo de dado)
            return JsonResponse({"error": str(e)}, status=400)

    # Caso o método não seja POST
    return JsonResponse({"error": "Método não permitido"}, status=405)


