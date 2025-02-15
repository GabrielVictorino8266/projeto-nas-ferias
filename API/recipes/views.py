from django.http import JsonResponse, HttpResponse
from .mongodb import get_all_recipes, save_recipe, delete_recipe, get_all_users, save_user, get_data_author
import json
from datetime import datetime, timezone
from .validations import validate_recipe_data, validate_user_data
from django.views.decorators.http import require_http_methods


def RecipeListView(request):
    # Obter todas as receitas
    if request.method == "GET":
        recipes = get_all_recipes()
        # Retornar as receitas como uma resposta JSON
        return JsonResponse({"recipes": recipes})
    else:
        return JsonResponse({"error": "Método não permitido"}, status=405)


def Home(request):
    return HttpResponse('''
        <div style="text-align: center;" >
            <h2 style="font-weight: bold;">Endpoints:</h2>
            <table border="1" style="margin: auto; border-collapse: collapse; width: 50%;">
                <tr>
                    <th style="padding: 8px; background-color: #f2f2f2;">Method</th>
                    <th style="padding: 8px; background-color: #f2f2f2;">Endpoint</th>
                </tr>
                <tr>
                    <td style="padding: 8px;">GET</td>
                    <td style="padding: 8px;">/recipes</td>
                </tr>
                <tr>
                    <td style="padding: 8px;">POST</td>
                    <td style="padding: 8px;">/recipes/new</td>
                </tr>
                <tr>
                    <td style="padding: 8px;">DELETE</td>
                    <td style="padding: 8px;">recipes/delete/</td>
                </tr>
                <tr>
                    <td style="padding: 8px;">GET</td>
                    <td style="padding: 8px;">/users</td>
                </tr>
                <tr>
                    <td style="padding: 8px;">POST</td>
                    <td style="padding: 8px;">/users/new</td>
                </tr>
            </table>
        </div>
    ''')


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
            user_id = data.get("user")

            user = get_data_author(user_id)

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

            #recipe_id = save_recipe(title, description, ingredients, instructions, creation_date, ratings, user)
            recipe_id = 0000000000

            return JsonResponse({"message": "Receita adicionada!", "id": str(recipe_id)}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido"}, status=400)

        except ValueError as e:
            # Captura de erro de validação (como erro no tipo de dado)
            return JsonResponse({"error": str(e)}, status=400)

    # Caso o método não seja POST
    return JsonResponse({"error": "Método não permitido"}, status=405)

@require_http_methods(["DELETE"])
def Delete_Recipe(request, id):
    """
    Deletes a recipe from the database.
    This function handles the deletion of a recipe identified by its unique ID.
    Raises:
        RecipeNotFoundError: If the recipe does not exist.
        PermissionError: If the user does not have permission to delete the recipe. (it will be implemented in the future)
    """
    recipe_id = id
    if not recipe_id:
        return JsonResponse({"error": "ID não fornecido"}, status=400)
    
    deleted_count = delete_recipe(recipe_id)

    if deleted_count == 0:
        return JsonResponse({"error": "Receita não encontrada"}, status=404)

    return JsonResponse({"message": "Receita deletada!"}, status=200)



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


