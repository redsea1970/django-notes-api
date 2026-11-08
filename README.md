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

# Django Notes API

REST API для управления заметками на Django + DRF.

## 🚀 Возможности
- Регистрация пользователей (`/api/register/`).
- Токен-авторизация.
- CRUD для заметок (`/api/notes/`).
- Изоляция данных: каждый пользователь видит только свои заметки.

## 🛠 Технологии
- Python 3.12, Django, Django REST Framework
- SQLite
- Pytest / Django TestCase (4 теста)

## 📦 Установка и запуск
```bash
# Клонировать репозиторий
git clone https://github.com/redsea1970/django-notes-api.git

# Создать и активировать виртуальное окружение
python -m venv .venv
source .venv/bin/activate

# Установить зависимости
pip install -r requirements.txt

# Применить миграции
python manage.py migrate

# Запустить сервер
python manage.py runserver
## Автор
redsea1970

## Архитектура

Подробная схема проекта: [ARCHITECTURE.md](ARCHITECTURE.md)
