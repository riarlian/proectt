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
