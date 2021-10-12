# Useful Commands

Here we have some commands that we will need.

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








