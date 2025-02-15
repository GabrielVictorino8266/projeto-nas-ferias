# 📌JSON Example for Recipe Registration

```json
{
  "title": "Bolo Surpresa",
  "user": "67ae81811fe302ad5bbe6886",
  "description": "Uma receita deliciosa e fácil para um bolo surpresa!",
  "ingredients": [
    "2 xícaras de farinha de trigo",
    "1 xícara de açúcar",
    "3 ovos",
    "1/2 xícara de óleo",
    "1 xícara de leite",
    "1 colher de sopa de fermento em pó",
    "1 pitada de sal"
  ],
  "instructions": "Misture todos os ingredientes até obter uma massa homogênea."
}
```


# 📌JSON Example for User Registration

```json
{
    "name": "Pedro Santos",
    "email": "pedro.santos@example.com",
    "password": "senha12345"
  }
```

# DELETE /recipes/delete/id/
Request
- Method: DELETE
- URL: http://localhost:8000/recipes/delete/id/
Replace the id by object id of a document.

### Response
- Success Response:
  - Code: 200 OK
  - Content:
  ```json
  {
    "message": "Receita deletada!"
  }
  ```

Error Responses:
  - Code: 400 Bad Request
  
    - Content:
    ```json
      {
        "error": "ID não fornecido"
      }
    ```
    
    - Content:
    ```json
      {
        "error": "ID não fornecido"
      }
    ```
Code: 404 Not Found

  - Content:
    ```json
      {
        "error": "Receita não encontrada"
      }
    ```