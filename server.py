import json
from flask import Flask, abort
from mock_data import catalog




app = Flask("Server")


@app.route("/")
def home():
    return "Hello from Flask"



@app.route("/me")
def about_me():
    return "Daniel Chavez"




#############################################
##########  API ENDPOINTs   #################
##########   RETURN JSON    #################
#############################################


@app.route("/api/catalog", methods=["get"])
def get_catalog():
    return json.dumps(catalog)

@app.route("/api/catalog", methods=["post"])
def save_product():
    pass


# GET /api/catalog/count -> how many products exist in the catalog
@app.route("/api/catalog/count")
def product_count():
    count = len(catalog)
    return json.dumps(count)


# get /api/catalog/total -> the sum of all product's prices
@app.route("/api/catalog/total")
def total_of_catalog():
    total = 0
    for prod in catalog:
        total += prod["price"]

    return json.dumps(total)


@app.route("/api/product<id>")
def get_by_id(id):
# find the product with _id is equal to id
    for prod in catalog:
        if prod["_id"] == id:
            return json.dumps(prod)


    return abort(404, "No product with such id")


@app.route("api/product/cheapest")
def cheapest_product():
    
    solution = catalog[0]
    for prod in catalog:
        if prod["price"] < solution["price"]:
            solution = prod

    return json.dumps(solution)






@app.route("api/product/cheapest")
def cheapest_product():
    
    categories = []
    for prod in catalog:
        catagory = prod["category"]
        if not category in categories["price"]:
            categories.append(category)

    return json.dumps(categories)




@app.get("/api/catalog/<category")
def prods_by_category(category):
    result = []
    for prod in catalog:
        if prod["category"] == category:
            result.append(prod)


    return json.dumps(result)
    



app.run(debug=True)