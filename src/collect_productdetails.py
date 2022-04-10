import scrapper as _scrapper

def makejsonFile(prod : str):
   product_details =  _scrapper.product_searched(prod)
   with open("productdetails.json", "w") as outfile:
        outfile.write(product_details)

