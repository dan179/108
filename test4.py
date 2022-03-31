from mock_data import catalog

def find_prod():
    text = "y"


    count = 0
    for prod in catalog:
        title = prod["title"]
        if text.lower() in title.lower():
                print(f"{title} $ {prod['price]}")








def unique_catagories():
    catagories = []
    for prod in catalog
        catagory = prod["category"]
        if not catagory in catagories:
            catagories.append(catagory)

    print(catagories)







find_prod()
unique_catagories()