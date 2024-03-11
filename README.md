# LAB - Class 33

## Project: Authentication & Production Server

### Author: Johnny Backus

### Links and Resources

- [CodeFellows Python Lab Instructions](https://codefellows.github.io/code-401-python-guide/reference/submission-instructions/labs/)
- [CodeFellows README template](https://codefellows.github.io/code-401-python-guide/reference/submission-instructions/labs/README-template.html)
- lecture demo code used for reference
- GitHub CoPilot chat feature used to uncover error caused by modifying model after making migtations

### Setup

- *.env requirements: n/a*
- must have Docker

### How to Initialize/Run Your Application

- Enter CLI command `docker compose build`
- Enter CLI command `docker compose up`
- View content in local port indicated in terminal
- path to booklist is /api/v1/books/

### How to Use Your Library

- n/a

### Tests

#### How to Run Tests

- with Docker running, use CLI command `docker compose exec web python manage.py test`
- ThunderClient was used for JWT testing.
- Obtain an access token via Post and using url: http://0.0.0.0:8000/api/token/
- in Body --> JSON, use existing username and password. For example:

```python
{
"username": "username"
"password": "password"
}
```

#### Tests of Note

- Tests for CRUD; user access token will need to be pasted to Auth --> Bearer Token
- The token should allow use of GET and POST at url http://0.0.0.0:8000/api/v1/books/
- For POST, the Body --> JSON would look something like this:

```python
{
    "owner": 2,
    "title": "test book",
    "author": "Fake Author",
    "publication_year": 1980
}
```

PUT and DELETE methods are restricted the book owner, which is most easily visualized on the deployed gunicorn server.

#### Incomplete Tests

- n/a
