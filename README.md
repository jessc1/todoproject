Todo List API

utilizei o framework django e django rest framework para o desenvolvimento pois é uma arquitetura monolítica na qual posso integrar todos os components em uma aplicação.

## Endpoints:
* To get access to the api is necessary to register in  http://127.0.0.1:8000/api/auth/register/, with the username, email and password,
   copy the refresh token in the http://127.0.0.1:8000/api/auth/refresh/ to get the access token, then copy the access token in the others endpoints
* Login:  http://127.0.0.1:8000/api/auth/login/
* Users : list of users http://127.0.0.1:8000/api/users/
* User detail http://127.0.0.1:8000/api/users/id/
* Tasks List: http://localhost:8000/api/tasks/ http methods: post, put, delete
* Task detail: http://localhost:8000/api/tasks/id
* Filter task: http://localhost:8000/api/tasks/?search=task
* register um user in the frontend http://localhost:3000/register/ 
* login: http://localhost:3000/login/  (fiz somente essa funcionalidade no front, pois só comecei depois que terminei o back, ontem.)

commands:

 utilizei o uv package manager, segue comandos:

 start the django server
```
 uv run python manage.py runserver
```

 to create database migration
```
 uv run python manage.py  makemigrations
```

applying  the migration
```
uv run python manage.py migrate
```
Para rodar os testes
```
uv run pytest
```

para rodar o clientapp frontend
```
npm start
```
