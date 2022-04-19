from datetime import datetime
from fastapi import Depends, FastAPI ,HTTPException,status
import models, database, service , schemas
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=database.engine)


app = FastAPI()

async def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
 



#route de recuperation du menu en fonction de la date
@app.get("/api/menu/{date_of}")
def the_menu(date_of: datetime , db : Session = Depends(get_db)):
    dishes = list(service.get_dish_by_date(db,date_of))
    beverages = (service.get_bevarage_by_date(db, date_of))
    menu = dict(dishes = dishes, beverages = beverages)
    return menu

 #route de recuperation de recuperationdes differents plats
@app.get("/api/dishes")
def dishes(db: Session = Depends(get_db)):
    return service.get_all_dishes(db)

#route de recuperation des ddifferentes boissons
@app.get("/api/beverages")
def dishes(db: Session = Depends(get_db)):
    return service.get_all_beverages(db)

#route de recuperation des differentes commandes
@app.get("/api/orders")
def orders(db: Session = Depends(get_db)):
    return service.get_all_orders(db)

#route de creation de d'un plat
@app.post("/api/create/dish")
def create_dish( dish : schemas.DishesCreate, db : Session = Depends(get_db)):
    dish_obj = service.get_dish_by_name(db,dish)
    if dish_obj :
        return service.create_dish(db, dish)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="there is already this dish ")

#route de creation d'une boisson
@app.post("/api/create/beverage")
def create_beverage( beverage : schemas.BeverageCreate, db : Session = Depends(get_db)):
    beverage_obj = service.get_beverage_by_name(db, beverage)
    if beverage_obj :
        return service.create_beverage(db, beverage)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="there is already this dish ")


