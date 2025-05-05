from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

body_types = [
    "Sedan",
    "Hatchback",
    "SUV",
    "Crossover",
    "Coupe",
    "Convertible",
    "Wagon",
    "Pickup",
    "Minivan",
    "Van"
]

def main():
    db: Session = SessionLocal()
    for name in body_types:
        exists = db.query(models.BodyType).filter(models.BodyType.name == name).first()
        if not exists:
            body_type = models.BodyType(name=name)
            db.add(body_type)
    db.commit()
    db.close()
    print("Типы кузова добавлены!")

if __name__ == "__main__":
    main()
