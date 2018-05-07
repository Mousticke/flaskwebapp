# First Web application using Python and Flask

### Installation :
```python 
    pip install -r INSTALL.txt
```

### Configuration
You need to put in you env variable :
- SECRET_KEY
- SQLALCHEMY_DATABASE_URI
- EMAIL_USER
- EMAIL_PASS

See the file `config.py`

### API
To consume the api, use `http://127.0.0.1:5000/api/v1`

### Available endpoints
- /users
    - `GET : /users`
    - `GET : /users/<int:id>`
    - `POST :/users`
- /posts
    -  `GET : /posts`
    - `GET : /posts/<int:id>`

### Todos
- Build basic web app
- Pass into RESTful API
- See the git repository in Post
- Use a config file with mongoose database
- Use a config file with multipe use cas (mail server, databse...)