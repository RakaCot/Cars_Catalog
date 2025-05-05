from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

time_counter = 0

@router.get("/now")
def current_time():
    global time_counter
    time_counter += 1
    return {"current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

@router.get("/now/count")
def show_count():
    return f"The current time page was requested {time_counter} times"
