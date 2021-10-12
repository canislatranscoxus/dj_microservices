# Useful Commands

Here we have some commands that we will need.

### Create virtual Environment

```
sh
python -m venv env
```


### Activate virtual Environment

```
sh
source ~/git/dj_microservices/kishan/env/bin/activate
```


### Install requisites

```
sh
cd ~/git/dj_microservices/kishan
python -m pip install -r requirements.txt
```

### create a django project

```
sh
django-admin startproject my_proj
django-admin startproject djangoRestAPI_project
```


### create a django app

```
sh
python manage.py startapp my_app
python manage.py startapp actors_app
```

### make database migration files

```
sh
python manage.py makemigrations
```

### migrate objetcs to database

```
sh
python manage.py migrate
```

### create superuser

```
sh
python manage.py createsuperuser
```

### run django server

```
sh
python manage.py runserver
```

### Test Rest API - GET method

go to 
http://127.0.0.1:8000

or in a terminal
```
sh
curl http://127.0.0.1:8000/

curl http://127.0.0.1:8000/ | python -m json.tool

curl -X GET http://127.0.0.1:8000/ | python -m json.tool
```

### Test Rest API - POST method

```
sh
curl -X POST http://127.0.0.1:8000/ \
-H 'content-type: application/json' \
-d  '{ "name" : "Kim Kardashian", "age" : "33" }' \
| python -m json.tool
```







