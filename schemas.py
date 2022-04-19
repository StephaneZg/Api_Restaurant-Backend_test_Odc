from datetime import datetime
from enum import Enum
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):

    full_name : str
    phone_number : str
    email : EmailStr


class UserCreate(UserBase):
    password : str


class User(UserCreate):
    id : int
    is_deleted : bool

    class config():
        orm_mode = True


class DishesBase(BaseModel):

    dish_name : str
    price : int
    is_delivery : bool
    created_at : str
    available_at : datetime
    

class DishesCreate(DishesBase):
    pass


class Dishes(DishesBase):
    id : int
    user_id :int
    is_deleted : bool

    class config():
        orm_mode = True


class OrdersBase(BaseModel):
    dish_name : str
    delivery_date : str 
    delivery_hour : str
    delivery_place :str
    customer_phone : str


class OrdersCreate(DishesBase):
    pass


class Orders(DishesBase):

    id :int
    dish_name : str
    delivery_date : str 
    delivery_hour : str
    delivery_place :str
    customer_phone : str
    is_deleted : bool

    class config():
        orm_mode = True


class ModelCat(str, Enum):
    jus_naturel = "Jus Naturel"
    vin = "Vin"
    biere = "Biere"


class BeverageBase(BaseModel):

    title : str
    price : float
    categorie : ModelCat
    available_at : datetime


class BeverageCreate(BeverageBase):

    pass


class Beverage(BeverageBase):
    id : int
    is_deleted : bool

    class config():
        orm_mode = True

