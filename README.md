# Финальный проект. API для YaTube.

***

## Описание
API социальной сети для публикации личных дневников. Сервис поддерживает 
возможности:
- отправление постов (с публикацией изображений и категоризацией по 
существующим тегам); 
- отправление комментариев к постам;
- подписка на интересующих авторов.

***

### Технологии
- Python 3.x
- Django 3.2
- DRF
- JWT
Полный перечень библиотек указан в файле requirements.txt

***

### Установка и запуск проекта
1. Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/taube-a/api_final_yatube.git

cd api_final_yatube
```
2. Создать и активировать виртуальное окружение:
- для MacOS:
```
python3 -m venv <venv_name>

source <venv_name>/bin/activate

python3 -m pip install --upgrade pip
```
- для Windows:
```
python -m venv <venv_name> 

source <venv_name>/Scripts/activate

python -m pip install --upgrade pip
```
3. Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
4. Выполнить миграции:
- для MacOS:
```
cd yatube_api
python3 manage.py makemigrations
python3 manage.py migrate
```
- для Windows:
```
cd yatube_api
python manage.py makemigrations
python manage.py migrate
```
5. Запустить проект:
- для MacOS:
```
python3 manage.py runserver
```
- для Windows:
```
python manage.py runserver
```

### Документация
Документация по проекту доступна по адресу: 
```
http://127.0.0.1:8000/redoc/
```

***

## Примеры использования API
<!--- примеры запросов к API --->