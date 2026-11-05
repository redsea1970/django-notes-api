# Django Notes API

CRUD-приложение «Заметки» с регистрацией, авторизацией, админкой и REST API.

## Что внутри
- Django + Django REST Framework.
- Модель Note (заголовок, текст, автор, дата).
- Регистрация и авторизация.
- Админка для управления заметками.
- REST API: список, создание, редактирование, удаление.
- Демо-режим: SQLite (в Live — PostgreSQL).

## Стек
- Python 3.14
- Django 5.x
- Django REST Framework
- SQLite (демо) / PostgreSQL (Live)

## Как запустить
1. Установить зависимости: pip install -r requirements.txt
2. Применить миграции: python manage.py migrate
3. Создать суперпользователя: python manage.py createsuperuser
4. Запустить: python manage.py runserver
5. Открыть: http://127.0.0.1:8000/api/notes/

## Автор
redsea1970

## Архитектура

Подробная схема проекта: [ARCHITECTURE.md](ARCHITECTURE.md)
