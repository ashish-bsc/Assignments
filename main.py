from fastapi import FastAPI
import collect_productdetails as colProd
from typing import Dict
import json as _json

app = FastAPI()

@app.get("/")
async def root(ProductName :str):
    colProd.makejsonFile(ProductName)
    return get_all_products()

def get_all_products() -> Dict:
    with open("productdetails.json", "r") as product_file:
        data = _json.load(product_file)

    return data