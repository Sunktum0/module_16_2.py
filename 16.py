from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from typing import Annotated
from fastapi import Path

# Создаем экземпляр FastAPI
app = FastAPI()

# Маршрут к главной странице
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "Главная страница"

# Маршрут к странице администратора
@app.get("/user/admin", response_class=HTMLResponse)
async def read_admin():
    return "Вы вошли как администратор"

# Маршрут для получения пользователя по ID
@app.get("/users/{user_id}")
async def get_user(
    user_id: Annotated[int, Path(gt=0, le=100, description="Enter User ID")]
):
    return {"user_id": user_id}

# Маршрут для получения информации о пользователе с параметрами в запросе
@app.get("/user/{username}/{age}")
async def read_user_info(
    username: Annotated[str, Path(
        min_length=5,
        max_length=20,
        description="Введите username (от 5 до 20 символов)"
    )],
    age: Annotated[int, Path(
        ge=18,
        le=120,
        description="Введите age (от 18 до 120)"
    )]
):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"