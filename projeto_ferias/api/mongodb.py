from pymongo import MongoClient
import environ

# Lê o arquivo .env
env = environ.Env()
environ.Env.read_env()  # Carrega as variáveis do .env

# Carregar a URI de conexão com o MongoDB
MONGO_URI = env("MONGO_URI")
mongo_client = MongoClient(MONGO_URI)

# Acessar o banco de dados "projetoferias"
mydb = mongo_client["projetoferias"]


# Acessar a coleção de receitas
recipes_collection = mydb.recipes

def get_all_recipes():
    recipes = list(recipes_collection.find())

 # Converter ObjectId para string para evitar erro de serialização
    formatted_recipes = []
    for recipe in recipes:
        recipe["_id"] = str(recipe["_id"])  # Converte o ObjectId para string
        
        # Se o author for uma referência de usuário, apenas obtém o id do usuário
        if recipe.get('author'):
            recipe['author'] = str(recipe['author'])  # Converte o author (ObjectId) para string
        
        formatted_recipe = {
            "id": recipe.get("_id"),  # Agora é uma string
            "title": recipe.get("title"),
            "description": recipe.get("description"),
            "ingredients": recipe.get("ingredients"),
            "instructions": recipe.get("instructions"),
            "author": recipe.get("author"),  # O author agora é uma string (ObjectId)
            "ratings": recipe.get("ratings"),
        }
        formatted_recipes.append(formatted_recipe)

    return formatted_recipes
