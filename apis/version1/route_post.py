from fastapi import APIRouter, HTTPException
from db.models.post_content import Product
from db.repository.post import create_new_post, get_product_by_id, get_products
from db.session import get_db, engine
from fastapi import Depends, UploadFile, File
from schemas.post_contents import CreateProduct, UpdateProduct
from sqlalchemy.orm import Session
from typing import List


router = APIRouter()

@router.post("/")
def create_post_contents(posts: CreateProduct = Depends(), file: UploadFile = File(...), db: Session = Depends(get_db)):
    post_contents = create_new_post(post=posts, files=file.filename, db=db)
    return post_contents


@router.get("/{product_id}")
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = get_product_by_id(product_id=product_id, db=db)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.get("/allproducts/")
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = get_products(db, skip=skip, limit=limit)
    return products

@router.patch("/{product_id}")
def update_product(product_id: int, product: UpdateProduct):
    with Session(engine) as session:
        db_product = session.get(Product, product_id)
        if not db_product:
            raise HTTPException(status_code=404, detail="Product not found")
        product_update = product.dict(exclude_unset=True)
        for key, value in product_update.items():
            setattr(db_product, key, value)
        session.add(db_product)
        session.commit()
        session.refresh(db_product)
        return db_product

@router.delete("/delete/{product_id}")
def delete_product(product_id: int):
    with Session(engine) as session:
        product = session.get(Product, product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        session.delete(product)
        session.commit()
        return {"Product": "Product Deleted Successfully"}