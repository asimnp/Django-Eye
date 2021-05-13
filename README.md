# Django Eye
> Django starter project to build django project quickly with powerful tools.

## Installation
Django Eye can be installed via Pip or Pipenv. To start, clone the repository to your local computer.
```shell
$ git clone https://github.com/alex1the1great/Django-Eye.git
$ cd Django-Eye
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
**Migrate**
```shell
$ python manage.py migrate --settings=root.settings.development
```

**Run Django Server**
```shell
$ python manage.py runserver --settings=root.settings.development
```
## 🤝 Contributing
Contributions, issues and feature requests are welcome!
## ⭐️ Support
Give a ⭐️ if this project helped you!