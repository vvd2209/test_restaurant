# Тестовое задание backend разработчик UTF.tech

Этот проект предоставляет API для вывода меню ресторана с категориями блюд и их деталями. Используется Django и Django REST Framework для создания сервера, который обрабатывает запросы и возвращает данные о категориях и блюдах.

## Установка

1. Клонируйте репозиторий:

    git clone https://github.com/vvd2209/test_restaurant
   
    cd restaurant

3. Создайте и активируйте виртуальное окружение:

    python3 -m venv venv
   
    source venv/bin/activate  # Для Linux/Mac
    venv\Scripts\activate     # Для Windows

5. Установите зависимости:   

    pip install -r requirements.txt

6. Выполните миграции:

   python manage.py migrate

7. Создайте суперпользователя для админки:

    python manage.py createsuperuser
   
8. Запустите сервер:

   python manage.py runserver

9. Откройте браузер и перейдите по адресу:
   
   http://127.0.0.1:8000/api/v1/foods/


## Описание API
Получить список категорий с блюдами
URL: /api/v1/foods/

Метод: GET

Описание: Возвращает список всех категорий меню с их блюдами, при этом включаются только опубликованные блюда (is_publish=True).   

## Технологии
Python 3.12

Django 4.x

Django REST Framework

SQLite (по умолчанию, можно настроить на другую базу данных)
