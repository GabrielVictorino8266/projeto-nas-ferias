from mongoengine import Document, StringField, IntField, DateTimeField, ListField, ReferenceField, FloatField, Q, connect
from datetime import datetime

connection_string:str = 'mongodb+srv://gabrielvictorino2004:R0BfA7OdqR9JjVy5@cluster0.capw8.mongodb.net/'
connect(
    db="projetoferias",
    host="mongodb+srv://gabrielvictorino2004:R0BfA7OdqR9JjVy5@cluster0.capw8.mongodb.net/"
)

class User(Document):
    meta = {'collection':'users'}
    name = StringField(required=True)
    email = StringField(required=True)
    password = StringField(required=True)
    creation_date = DateTimeField(default=datetime.now)
    favorites = ListField(StringField())
    created_recipes = ListField(StringField())

class Recipe(Document):
    meta = {'collection':'recipes'}
    title = StringField(required=True)
    description = StringField(required=True)
    ingredients = ListField(StringField())
    instructions = StringField()
    creation_date = DateTimeField(default=datetime.now)
    author = ReferenceField(User)
    ratings = ListField(FloatField())


# # Criando receitas
# recipes = [
#     Recipe(title="Bolo de Cenoura", description="Um bolo simples e delicioso com cobertura de chocolate.",
#            ingredients=["cenoura", "farinha", "açúcar", "ovos", "chocolate"],
#            instructions="Misture os ingredientes, asse por 40 minutos e adicione a cobertura.",
#            author=User.objects(name="Ana Silva").first(),
#            ratings=[5, 4, 5]),
#     Recipe(title="Feijoada", description="Tradicional prato brasileiro com feijão preto e carnes.",
#            ingredients=["feijão preto", "carne de porco", "linguiça", "tempero"],
#            instructions="Cozinhe o feijão e as carnes separadamente, depois misture e tempere.",
#            author=User.objects(name="Carlos Oliveira").first(),
#            ratings=[4, 5, 5]),
#     Recipe(title="Panqueca de Frango", description="Panquecas recheadas com frango desfiado.",
#            ingredients=["farinha", "ovos", "leite", "frango desfiado", "molho de tomate"],
#            instructions="Prepare a massa, recheie com frango e cubra com molho.",
#            author=User.objects(name="Ana Silva").first(),
#            ratings=[3, 4]),
#     Recipe(title="Pizza Margherita", description="Pizza italiana com molho de tomate, mussarela e manjericão.",
#            ingredients=["massa de pizza", "molho de tomate", "mussarela", "manjericão"],
#            instructions="Monte a pizza e asse por 20 minutos.",
#            author=User.objects(name="Mariana Souza").first(),
#            ratings=[5, 5, 4]),
#     Recipe(title="Lasanha de Berinjela", description="Uma opção leve de lasanha feita com fatias de berinjela.",
#            ingredients=["berinjela", "molho de tomate", "queijo", "carne moída"],
#            instructions="Monte a lasanha e asse até dourar.",
#            author=User.objects(name="Mariana Souza").first(),
#            ratings=[4, 4])
# ]

# # inserting a person
# users:list = [
#     User(name="Ana Silva", email="ana.silva@example.com", password="hashed_senha_ana", favorites=["recipe2", "recipe5"], created_recipes=["recipe1", "recipe3"]),
#     User(name="Carlos Oliveira", email="carlos.oliveira@example.com", password="hashed_senha_carlos", favorites=["recipe1", "recipe4"], created_recipes=["recipe2"]),
#     User(name="Mariana Souza", email="mariana.souza@example.com", password="hashed_senha_mariana", favorites=["recipe3"], created_recipes=["recipe4", "recipe5"]),
#     User(name="Pedro Santos", email="pedro.santos@example.com", password="hashed_senha_pedro", favorites=[], created_recipes=[]),
#     User(name="Juliana Pereira", email="juliana.pereira@example.com", password="hashed_senha_juliana", favorites=["recipe2"], created_recipes=[])
# ]

# for user in users:
#     user.save()

# # Salvando receitas no banco
# for recipe in recipes:
#     recipe.save()

# # Printing data
# for user in User.objects:
#     print(user.name)

for recipe in Recipe.objects:
    if len(recipe.ratings) >= 3:
        print(recipe.title)

recipes = Recipe.objects(Q(ratings__gt=3))


users = User.objects(Q(name__icontains="Ana"))

for recipe in recipes:
    print(recipe.title, recipe.description)