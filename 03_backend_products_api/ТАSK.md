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