from fastapi import FastAPI, Depends
from models import Product
from dbconfig import session, engine
import db_models
from sqlalchemy.orm import Session

app = FastAPI()

db_models.Base.metadata.create_all(bind=engine)

Products = [
    Product(id=1,name="Phone",price=299),
    Product(id=2,name="Laptop",price=499),
    Product(id=3,name="Tablet",price=399),
]


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


def init_db():
    db = session()
    count = db.query(db_models.Product).count()
    
    if count == 0:
        for product in Products:
            db.add(db_models.Product(**product.model_dump()))
        
        db.commit()

init_db()


@app.get("/")
def greet():
    return "Hello Idiot"



@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    db_products = db.query(db_models.Product).all()
    return db_products



@app.get("/products/{id}")
def get_product_by_id(id: int,db: Session = Depends(get_db)):
    db_product = db.query(db_models.Product).filter(db_models.Product.id == id).first()
    if db_product:
        return db_product
    else:
        return "Product Not Found"



@app.post("/products")
def create_product(new_product: Product, db: Session = Depends(get_db)):
    db.add(db_models.Product(**new_product.model_dump()))
    db.commit()
    return "Product Created"



@app.put("/products/{id}")
def update_product(id: int,new_product:Product,db: Session = Depends(get_db)):
    db_product = db.query(db_models.Product).filter(db_models.Product.id == id).first()
    if db_product:
        db_product.name = new_product.name
        db_product.price = new_product.price
        db.commit()
        return "Product Updated"
    else:
        return "Product Not Found"



@app.delete("/products/{id}")
def delete_product(id: int,db: Session = Depends(get_db)):
    db_product = db.query(db_models.Product).filter(db_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Product deleted"
    else:
        return "Product Not Found"