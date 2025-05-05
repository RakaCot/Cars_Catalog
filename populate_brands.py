from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

brands = [
    "Toyota",
    "BMW",
    "Mercedes-Benz",
    "Audi",
    "Ford",
    "Honda",
    "Kia",
    "Hyundai",
    "Volkswagen",
    "Lada"
]

def main():
    db: Session = SessionLocal()
    for name in brands:
        exists = db.query(models.Brand).filter(models.Brand.name == name).first()
        if not exists:
            brand = models.Brand(name=name)
            db.add(brand)
    db.commit()
    db.close()
    print("Бренды добавлены!")

if __name__ == "__main__":
    main()