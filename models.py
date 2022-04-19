from datetime import datetime
from sqlalchemy import Boolean, Column , Integer , String, TIMESTAMP, null,DATETIME
from sqlalchemy.orm import relationship

from database import Base


#model de la table des utilisateurs
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, Primary_key = True)
    full_name = Column(String)
    phone_number = Column(String)
    email = Column(String)
    is_deleted = Column(Boolean, default = False)

#model de la table des plats
class Dishes(Base):
    __tablename__ = "dishes"

    id = Column(Integer, Primary_key = True)
    dish_name = Column(String)
    price = Column(String)
    is_delivery = Column(Boolean)
    created_at = Column(DATETIME, default = datetime.now())
    available_at = Column(DATETIME)
    is_deleted = Column(Boolean, default = False)

#model de la table des commandes
class Orders(Base):
    __tablename__ = "orders"

    id = Column(Integer, Primary_key = True)
    dish_name = Column(String)
    delivery_date = Column(DATETIME)
    delivery_hour = Column(String)
    delivery_place = Column(String)
    customer_phone = Column(String)

    dish = relationship("Dishes", back_populates="dish")
    user = relationship("Users", back_populates="dish")

#model de la table des boissons
class Beverage(Base):
    __tablename__ = "beverages"

    id = Column(Integer,  Primary_key = True)
    title = Column(String)
    price = Column(String)
    available_at = Column(DATETIME)
    is_deleted = Column(Boolean, default = False)
    categories = Column(String)
