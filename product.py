from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

pro=[]

class products(BaseModel):
    Product_id: int
    Product_name: str
    Price: int
    Discription: str

@app.post("/Postproducts/")
def create_product(product: products):
    pro.append(product.dict())
    return{
        "msg": "Product added successfully",
        "data": pro
}

@app.get("/Getproducts/")
def get_product():
    return{
        "msg": "Product added successfully",
        "data": pro
}

    