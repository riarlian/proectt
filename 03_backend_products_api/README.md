# Backend Products API

Фамилия: Юсупова 
Имя: Даяна
Группа: ПИ-212 

## Описание

В данном репозитории содержится backend приложение для управления продуктами.

Приложение реализует REST API и позволяет:

- создавать продукты
- получать список продуктов
- обновлять продукты
- удалять продукты

## Используемые технологии

- Python
- Django
- Django REST Framework

## Установка и запуск

### 1. Клонировать репозиторий

git clone https://github.com/riarlian/proectt.git

### 2. Перейти в папку проекта

cd proectt/03_backend_products_api/app

### 3. Установить зависимости

pip install -r requirements.txt

### 4. Выполнить миграции

python manage.py migrate

### 5. Запустить сервер

python manage.py runserver 8082

### 6. Открыть API

http://127.0.0.1:8082/api/products/

## Скриншоты

### Список продуктов

![products](screens/products.png)

### Создание продукта

![create](screens/create_product.png)