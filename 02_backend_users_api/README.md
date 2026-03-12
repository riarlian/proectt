# Backend Users API

Фамилия: Юсупова 
Имя: Даяна
Группа: ПИ-212  

## Описание

В данном репозитории содержится backend приложение для управления пользователями.

Приложение реализует REST API и позволяет:

- создавать пользователей
- получать список пользователей
- обновлять пользователей
- удалять пользователей

## Используемые технологии

- Python
- Django
- Django REST Framework

## Установка и запуск

### 1. Клонировать репозиторий

git clone https://github.com/riarlian/proectt.git

### 2. Перейти в папку проекта

cd proectt/02_backend_users_api/app

### 3. Установить зависимости

pip install -r requirements.txt

### 4. Выполнить миграции

python manage.py migrate

### 5. Запустить сервер

python manage.py runserver 8081

### 6. Открыть API

http://127.0.0.1:8081/api/users/

## Скриншоты

### Список пользователей

![users](screens/users.png)

### Создание пользователя

![create](screens/create_user.png)

### Список пользователей

![users](screens/userlist.png)
