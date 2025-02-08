def validate_recipe_data(title, description, ingredients, instructions, ratings):
    # Validar se 'title' e 'description' são strings e maior que 0
    if not isinstance(title, str):
        raise ValueError("O título deve ser uma string.")
    if len(title) == 0:
        raise ValueError("O título está vazio")

    if not isinstance(description, str):
        raise ValueError("A descrição deve ser uma string.")
    if len(description) == 0:
        raise ValueError("A descrição está vazia")
    
    # Validar se 'ingredients' é uma lista e maior que 0
    if not isinstance(ingredients, list):
        raise ValueError("Os ingredientes devem ser uma lista.")
    if len(ingredients) == 0:
        raise ValueError("Os ingredientes estão vazios")
    
    # Validar se todos os elementos da lista de ingredientes são strings
    if not all(isinstance(ingredient, str) and ingredient.strip() for ingredient in ingredients):
        raise ValueError("Todos os ingredientes devem ser strings não vazias.")

    # Validar se 'instructions' é uma string e maior que 0
    if not isinstance(instructions, str):
        raise ValueError("As instruções devem ser uma string.")
    if len(instructions) == 0:
        raise ValueError("A receita não possui instruções")
    
    # Validar se 'ratings' é uma lista de inteiros e maior que 0
    if not isinstance(ratings, list):
        raise ValueError("As classificações devem ser uma lista.")
    
    if not all(isinstance(rating, int) for rating in ratings):
        raise ValueError("Todas as classificações devem ser inteiros.")

    return True
