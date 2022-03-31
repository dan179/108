


def test_dict():
    me = { 
        "first": "Daniel",
        "last": "Chavez",
        "age": 25,
        "hobbies": [mtb]
        "address": {
            "street": "Evergreen",
            "city": "Springfield",
        },
        "another" : 12,

    }

    print(me["first"] + " " + me["last"] )

    print("My age is: " + str(me["age"]))
    print(f"My age is: {me['age]}")

    address = me["address"]
    print(type(address))
    print(address)
    print(address["street"])

    print(me["address"]["city"])






    # add new keys 
    me["color"] = "red"

    # modify existing keys
    me ["age"] = 36

    # check if a key exist in a dict
    if "age" in me:
        print("Age exist")



print("---- Dictionary Test ----")
test_dict()