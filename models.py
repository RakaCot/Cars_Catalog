from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class Brand(Base):
    __tablename__ = "brands"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    cars = relationship("Car", back_populates="brand")

class BodyType(Base):
    __tablename__ = "body_types"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    cars = relationship("Car", back_populates="body_type")

class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, index=True)
    model = Column(String, index=True)
    brand_id = Column(Integer, ForeignKey("brands.id"))
    body_type_id = Column(Integer, ForeignKey("body_types.id"))
    price = Column(Integer)
    year = Column(Integer)

    brand = relationship("Brand", back_populates="cars")
    body_type = relationship("BodyType", back_populates="cars")
