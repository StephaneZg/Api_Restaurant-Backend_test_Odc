from datetime import datetime
from turtle import title
import schemas , models
from sqlalchemy.orm import Session



def get_dish_by_date(db : Session, date : datetime):
    return db.query(models.Dishes).filter(models.Dishes.available_at == date).all()


def get_bevarage_by_date(db : Session, date : datetime):
    return db.query(models.Beverage).filter(models.Beverage.available_at == date).all()


def get_all_dishes(db : Session):
    return db.query(models.Dishes).filter(models.Dishes.is_deleted == False).all()

def get_all_beverages(db : Session):
    return db.query(models.Beverage).filter(models.Beverage.is_deleted == False).all()

def get_all_orders(db : Session):
    return db.query(models.Orders).all()

def get_dish_by_name(db : Session, dish : schemas.Dishes):
    dishes = db.query(models.Dishes).filter(models.Dishes.dish_name == dish.dish_name.lower()).first()
    if dishes :
        return True
    else :
        return False

def create_dish(db : Session, dish):
    db_dish = models.Dishes(dish_name=dish.dish_name, price=dish.price,
     created_at = dish.created_at, available_at = dish.available_at, is_delivery = dish.is_delivery)
    db.add(db_dish)
    db.commit()
    db.refresh(db_dish)
    return db_dish

def get_beverage_by_name(db : Session, beverage : schemas.BeverageCreate):
    dishes = db.query(models.Beverage).filter(models.Beverage.title == beverage.title.lower()).first()
    if dishes :
        return True
    else :
        return False

def create_beverage(db : Session, beverage : schemas.BeverageCreate ):
    db_beverage = models.Dishes(title=beverage.title, price=beverage.price,
    available_at = beverage.available_at, categorie = beverage.categorie)
    db.add(db_beverage)
    db.commit()
    db.refresh(db_beverage)
    return db_beverage
