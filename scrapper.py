import requests as _requests
import bs4 as _bs4
import json as _json

def _generate_product_url(prod: str) -> str:
    url = f"https://www.bukalapak.com/products?from=omnisearch&from_keyword_history=false&search%5Bkeywords%5D={prod}&search_source=omnisearch_keyword&source=navbar"
    return url

def _get_page(url: str) -> _bs4.BeautifulSoup:
    page = _requests.get(url)
    soup = _bs4.BeautifulSoup(page.content, "html.parser")
    return soup

def product_searched(prod: str) -> _json:
    url = _generate_product_url(prod)
    page = _get_page(url)
    raw_prod = page.find_all(class_="bl-text bl-text--body-14 bl-text--ellipsis__2")
    prod_name = [prod_name.text.upper().replace("\n", "").strip() for prod_name in raw_prod]
    price_prod = page.find_all(class_="bl-text bl-text--subheading-20 bl-text--semi-bold bl-text--ellipsis__1")
    prod_price = [prod_price.text.replace("\n", "").strip() for prod_price in price_prod]
    store_prod = page.find_all(class_="bl-product-card__description-store")
    prod_store = [prod_store.text.replace("\n", "").strip() for prod_store in store_prod]
    score_titles = [{"ProductName": name, "Price": price, "Location" : loc} for name, price, loc in zip(prod_name, prod_price,prod_store)]

    return (_json.dumps(score_titles))
    