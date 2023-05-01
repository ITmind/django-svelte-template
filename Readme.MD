Не забываем создать пользователя админа
```bash
python manage.py createsuperuser
```
# При изменении модели

Делаем схему миграции
```bash
$ python manage.py makemigrations spa
```
Запускаем миграцию (создание/изменение таблиц)
```bash
$ python manage.py migrate
```