# First Web application using Python and Flask
> Pour toutes questions : contacter : akim.benchiha@gmail.com

### Installation :
```python 
    pip install -r INSTALL.txt
```

### Run :
```phyton 
    python run.py
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
        - Sorting : `?sorts=rank_asc` default `?sorts=rank_desc`
        - Pagination : `?page=1` default `no pagination`
        - Filtering : `?username=username` or `?email=email` or `?username=username&email=email`
    - `GET : /users/<int:id>`
    - `POST : /users`
    - `GET : /users/<int:id>/posts`
    - `GET : /users/<int:id>/posts/<int:post_id>`
        - Sorting : `?sorts=rank_asc` default `?sorts=rank_desc`
        - Pagination : `?page=1` default `no pagination`
- /posts
    -  `GET : /posts`
    - `GET : /posts/<int:id>`

### Todos
- [x] Build basic web app
- [ ] Pass into RESTful API (with searching, sorting, filtering and pagination)
- [ ] See the git repository in Post
- [x] Use a config file with multipe use cas (mail server, database...)