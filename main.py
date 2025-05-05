from fastapi import FastAPI
from routes import users, cars, time, fruits
from database import Base, engine

# Создаем все таблицы в базе (если еще нет)
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Подключаем роуты
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(cars.router, prefix="/cars", tags=["cars"])
app.include_router(time.router, prefix="/time", tags=["time"])
app.include_router(fruits.router, tags=["misc"])
