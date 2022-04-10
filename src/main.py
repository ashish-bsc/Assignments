from fastapi import FastAPI
import collect_productdetails as colProd
import json as _json

app = FastAPI()

@app.get("/")
def getProductDetails(ProductName :str):
    colProd.makejsonFile(ProductName)
    return get_all_products()

def get_all_products() -> _json:
    with open("productdetails.json", "r") as product_file:
        data = _json.load(product_file)

    return data