from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas, crud, auth
from database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.CarResponse)
def create_car(car: schemas.CarCreate, db: Session = Depends(get_db), current_user=Depends(auth.get_current_user)):
    return crud.create_car(db, car)

@router.get("/{car_id}", response_model=schemas.CarResponse)
def read_car(car_id: int, db: Session = Depends(get_db)):
    car = crud.get_car(db, car_id)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    return car

@router.get("/body_type/{body_type_name}")
def get_body_type_stats(body_type_name: str, db: Session = Depends(get_db)):
    cars = crud.get_cars_by_body_type(db, body_type_name)
    if cars is None:
        raise HTTPException(status_code=404, detail="Body type not found")
    if not cars:
        return {"message": "No cars found for this body type"}
    total_price = sum(car.price for car in cars)
    average_price = total_price / len(cars)
    return {
        "body_type": body_type_name,
        "total_cars": len(cars),
        "average_price": average_price
    }
