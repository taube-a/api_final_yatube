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

### Примечание
Доступ к созданию всего и просмотра некоторого контента сервиса 
предоставляется только при наличии токена.
Срок действия токена - 30 дней.

Инструкцию по созданию пользователя и можно найти ниже.

```

```

***

## Примеры использования API

Для формирования ответов и запросов будет использована программа Postman.

1. Создание нового пользователя

Придумайте пару «логин-пароль» и отправьте POST-запрос на http://127.0.0.1:8000/api/v1/users/, передав их в полях username и password.
Если вы всё сделали правильно, вам вернётся HTTP-ответ со статус-кодом 201 Created:
```
ссылка на изображение user_creating
```
2. Получение токена

Отправьте POST-запрос на эндпоинт http://127.0.0.1:8000/api/v1/jwt/create/, передав действующий логин и пароль в полях username и password.
Если вы всё сделали правильно, вам вернётся HTTP-ответ со статус-кодом 200 OK:
```
ссылка на изображение get_token
```
API вернёт JWT-токен:
```
# Пример ответа
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2OTg3MzQzNywianRpIjoiMTg4YTAyMTAyMWUxNDY5OWIyNTA2OTYxMDEzZWZkOWUiLCJ1c2VyX2lkIjoxfQ.o2GJ5Dfz2621IOxwbO0RmR_VUXewg7XqkqMsZUqBy-I",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcyMzc5MDM3LCJqdGkiOiJjOWYyMTc0YTQxMzc0ZDllOTk1Yjk1NzM1YTQyM2Q3MyIsInVzZXJfaWQiOjF9.e8XS_IwKaveQs17iRm3t9issRB56dr9X8t-Kg4bizD0"
}
```

Токен вернётся в поле access, а данные из поля refresh пригодятся для обновления токена.
Если ваш токен утрачен, украден или каким-то иным образом скомпрометирован, вам понадобится отключить его и получить новый. Для этого отправьте POST-запрос на тот же адрес /auth/jwt/create/, а в теле запроса в поле refresh передайте refresh-токен.
Этот токен также надо будет передавать в заголовке каждого запроса, в поле Authorization. Перед самим токеном должно стоять ключевое слово Bearer и пробел.
```
ссылка на изображение token_in_headers
```

3. Создание нового поста

Отправьте POST-запрос на эндпоинт http://127.0.0.1:8000/api/v1/posts/, передав обязательное поле "text".
Если вы всё сделали правильно, вам вернётся HTTP-ответ со статус-кодом 201 Created:
```
ссылка на изображение post_example
```

Полный список доступных эндпоинтов можно найти в домументации проекта. 

Автор: [Анастасия Таубе](https://github.com/taube-a)