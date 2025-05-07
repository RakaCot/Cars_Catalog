# Garage API

Backend-приложение на REST API для управлением автопарка (гаражом) с поддержкой пользователей, автомобилей,
брендов и типом кузова на FastAPI + SQLAlchemy + SQLite.

### Возможности
- Регистрация и аутентификация пользователей
- Добавление, просмотр, редактирование и удаление автомобилей
- Управление брендами и типами кузова
- REST API с документацией Swagger

### 🚀 Быстрый старт
>
> 1. Клонируйте репозиторий и перейдите в папку проекта:
>    
>    ```python
>    git clone <>
>    ```
>    ```python
>    cd Cars_Catalog
>    ```

> 2. Создайте и активируйте виртуальное окружение (рекомендуется):
>    
>    >    python -m venv venv
>    
>    * Для Windows:
>    >    venv\Scripts\activate
>    
>    * Для Linux/Mac:
>    >    source venv/bin/activate
>    
>
> 3. Установите зависимости:
>    
>    >    pip install -r requirements.txt
>    
>    Если файла requirements.txt нет, установите вручную:
>    >    pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose pydantic
>    

>
> 4. Запустите приложение:
>    
>    >    uvicorn main:app --reload
>    
>    Приложение будет доступно по адресу: http://127.0.0.1:8000/
>
> 5. Документация API:
>    
>    Swagger UI: http://127.0.0.1:8000/docs  <br> ReDoc: http://127.0.0.1:8000/redoc
>  
>    
>
>## 🧪 Запуск тестов
>    >    $env:PYTHONPATH = "."
>    pytest
>    
>## 📂 Структура проекта
>cars_catalog/<br>
>│<br>
>├── .pytest_cache/<br>
>├── routes/<br>
>│   ├── __init__.py<br>
>│   ├── cars.py<br>
>|   ├── fruits.py<br>
>│   ├── time.py<br>
>│   └── users.py<br>
>│<br>
>├── tests/<br>
>│   ├── __init__.py<br>
>│   └── test_basic.py<br>
>│<br>
>├── venv/<br>
>├── auth.py<br>
>├── crud.py<br>
>├── database.py<br>
>├── garage.db<br>
>├── main.py<br>
>├── models.py<br>
>├── populate_body_types.py<br>
>├── populate_brands.py<br>
>├── pylint.txt<br>
>└── schemas.py<br>

>## ⚙️ Основные возможности
>*Регистрация и аутентификация пользователей.
>
>*Управление автомобилями: добавление, просмотр, редактирование и удаление.
>
>*Работа с брендами и типами кузова (справочники).
>
>*Хранение данных в базе SQLite через SQLAlchemy.
>
>*REST API с поддержкой FastAPI и автогенерацией документации Swagger.
>
>*Тестирование базовых эндпоинтов.
>
>## 💡 Примечания
>* Все основные сущности (User, Car, Brand, BodyType) реализованы как SQLAlchemy-модели.

>* Для валидации данных используются Pydantic-схемы.

>* Скрипты populate_brands.py и populate_body_types.py наполняют справочники брендов и кузовов.
>## 🛠️ Частые команды
>* Запуск сервера:
>    >    uvicorn main:app --reload
>    
>* Запуск тестов:
>    >    $env:PYTHONPATH = "."
>    pytest
>    
>## 📝 Автор
> <b> Новиков Степан Сергеевич 
