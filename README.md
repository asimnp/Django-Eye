# Django Eye
> Django starter project to build django project quickly with powerful tools.

## Installation
Django Eye can be installed via Pip or Pipenv. To start, clone the repository to your local computer.
```shell
$ mkdir <your_directory_name>
$ cd <your_directory>
$ git clone https://github.com/alex1the1great/Django-Eye.git .
$ touch .env
$ cp .env.template .env
```


### Pip
```shell
$ python -m venv venv_djangoeye
$ source venv_djangoeye/bin/activate
$ pip install -r requirements.txt
```

### Pipenv
```shell
$ pipenv install
$ pipenv shell
```
**Django new secret key**
```shell
$ python manage.py shell
>>> from django.utils.cyrpto import get_random_string
>>> get_random_string(80)
# copy the secret key and assign it to DJANGO_SECRET_KEY
```
**PostgreSQL setup**
```
Create new postgresql database and add credentials into .env file.
```
**Migrate and run Django server**
```shell
$ python manage.py migrate
$ python manage.py runserver
```
**Delete .git directory**
```shell
$ rm -rf .git
```
**Create a new git repository**
```shell
$ git init
$ git add .
$ git commit -m "Initial setup"
```

**Create a new app**
```shell
$ cd apps
$ django-admin startapp <your_app_name>
```

**Register a newly created app**
- Go to [roots/settings/base.py](https://github.com/alex1the1great/Django-Eye/blob/master/root/settings/base.py)
```python
INSTALLED_APPS = [
    'apps.<your_app_name>.apps.<your_app_name>Config',
]
```

- Go to apps/<your_app>/apps.py
- Change the app name to:
    > name = 'apps.<your_app_name>'
```shell
$ cd ..
$ python manage.py runserver
```

**For production :exclamation:**
- Go to manage.py file and change settings file to production: 
  > *roots.settings.development*
  
  > *roots.settings.production*

## 🤝 Contributing
Contributions, issues and feature requests are welcome!
## ⭐️ Support
Give a ⭐️ if this project helped you!
