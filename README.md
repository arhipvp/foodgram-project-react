# Foodrgam

### Адрес сайта
```
http://158.160.37.99
```
login: arhvp
password: arhvp

"Продукторвый помощник" - сайт, где пользователи могут публиковать и редактировать свои рецепты, просматривать 
рецепты других пользователей и добавлять их в избранное и подписываться на авторов.
Также есть возможность скачать список продуктов, которые были добавлены в "Корзину".
Это поможет определиться с продуктовой корзиной в магазине

Проект реализован на `Django`.
Доступ к данным реализован через API-интерфейс.

## Развертывание проекта

### Развертывание на локальном сервере

- Установите на сервере `docker` и `docker-compose`.

- Создайте файл `/infra/.env`.
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
SECRET_KEY='ключ Django'
```
- Исполните команду `docker-compose up -d --build`.

- Совершите миграцию `docker-compose exec backend python manage.py migrate`.

- Создайте суперпользователя `docker-compose exec backend python manage.py createsuperuser`.

- Соберите статику `docker-compose exec backend python manage.py collectstatic --no-input`.

- Создайте пару тегов

## Автор проекта

Архипов Владимир Афанасьев