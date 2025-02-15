from pymongo import MongoClient
from bson.objectid import ObjectId
from django.http import JsonResponse
import environ

# Lê o arquivo .env
env = environ.Env()
environ.Env.read_env()  # Carrega as variáveis do .env

# Carregar a URI de conexão com o MongoDB
MONGO_URI = env("MONGO_URI")
mongo_client = MongoClient(MONGO_URI)

# Acessar o banco de dados "projetoferias"
mydb = mongo_client["projetoferias"]


# Acessar as coleções
recipes_collection = mydb.recipes
users_collection = mydb.users

def get_all_recipes():
    recipes = list(recipes_collection.find())

 # Converter ObjectId para string para evitar erro de serialização
    formatted_recipes = []
    for recipe in recipes:
        recipe["_id"] = str(recipe["_id"])  # Converte o ObjectId para string
        
        # Se o user for uma referência de usuário, apenas obtém o id do usuário
        if recipe.get('user'):
            recipe['user'] = str(recipe['user'])  # Converte o user (ObjectId) para string
        
        formatted_recipe = {
            "id": recipe.get("_id"),  # Agora é uma string
            "title": recipe.get("title"),
            "description": recipe.get("description"),
            "ingredients": recipe.get("ingredients"),
            "instructions": recipe.get("instructions"),
            "user": recipe.get("user"),  # O user agora é uma string (ObjectId)
            "ratings": recipe.get("ratings"),
            "creation_date": recipe.get("creation_date")
        }
        formatted_recipes.append(formatted_recipe)

    return formatted_recipes


def save_recipe(title, description, ingredients, instructions, creation_date, ratings, user):
    recipe = {
        "title": title,
        "user": user['_id'],
        "description": description,
        "ingredients": ingredients,
        "instructions": instructions,
        "ratings": ratings,
        "creation_date": creation_date,
    }
    result = recipes_collection.insert_one(recipe)
    return result.inserted_id



#-----------------------USERS----------------------------

def delete_recipe():
"""
This function delete a recipe from the database
"""
...

def get_all_users():
    users = list(users_collection.find())

    formatted_users = []
    for user in users:
        user["_id"] = str(user["_id"])
        
        if user.get('favorites'):
            user['favorites'] = str(user['favorites'])
        if user.get('created_recipes'):
            user['created_recipes'] = str(user['created_recipes'])

        formatted_recipe = {
            "id": user.get("_id"),
            "name": user.get("name"),
            "email": user.get("email"),
            "password": user.get("password"),
            "creation_date": user.get("creation_date"),
            "favorites": user.get("favorites"),
            "created_recipes": user.get("created_recipes"),
        }
        formatted_users.append(formatted_recipe)

    return formatted_users


def save_user(name, email, password, creation_date):
    user = {
        "name": name,
        "email": email,
        "password": password,
        "creation_date": creation_date,
        "favorites": list(),
        "created_recipes": list()
    }
    result = users_collection.insert_one(user)
    return result.inserted_id


def get_data_author(user_id):
    user = users_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        return user
    else:
        return JsonResponse({"error": "Usuário não encontrado"}, status=404)