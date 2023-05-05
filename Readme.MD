
# Описание

**Django + Svelte SPA + Docker + PostgreSQL + Unit (nginx)**

Шаблон Django в котором одна из страниц является SPA написанным на Svelte.
В качестве SPA сделано демо-приложение которое считывает и записывает данные в PostgreSQL.
(первоначально можно заполнить записи в таблице через админку)

В качестве web и app сервера выступает unit nginx.
Все настроено в Docker контейнере и готово к развертыванию на сервере.


# Разворачивание на сервере

Создать директорию на диске.

Клонировать репозиторий в созданную директорию:
```shell
git clone https://github.com/ITmind/django-svelte-template.git
```

Создать .env файл. В нем прописать свои логин/пароль

```dotenv
SECRET_KEY=my_secret_key
DEBUG=1
USE_POSTGRES=1

DATABASE_NAME=spa
DATABASE_HOST=db
DATABASE_PORT=5432

#создание административного пользователя при первом запуске контейнера
#или при python manage.py createsuperuser --noinput
DJANGO_SUPERUSER_PASSWORD=admin
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@django.com
#одновременно и для docker postgres и для Django
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```

Собрать и запустить контейнер Docker:
```shell
docker-compose up
```

Сайт доступен по порту :8000

*При запуске контейнера автоматически создается и делается миграция