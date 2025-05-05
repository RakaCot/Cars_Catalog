from fastapi import APIRouter
import random

router = APIRouter()

@router.get("/hello_world")
def hello_world():
    return "Hello, world!"

@router.get("/fruits")
def fruits():
    fruits_list = ["Apple", "Banana", "Orange", "Kiwi", "Lemon"]
    return {
        "fruits": fruits_list,
        "random_fruit": random.choice(fruits_list)
    }
