product =  {
    101:  {"name": "Laptop", "price": 99.99, "quantity": 20},
    102: {"name": "PC", "price": 200, "quantity": 10},
    103: {"name": "keyboard", "price":200 , "quantity": 200},
    104: {"name": "Mouse" , "price":100 , "quantity":200 },
    105: {"name": "speakers", "price":100 , "quantity":200 },
    106: {"name":"HEadphones" , "price":100 , "quantity":200 },
    107: {"name": "Xbox Controller", "price":100 , "quantity":200 },
    108: {"name":"PS4 Controller" , "price":100 , "quantity":200 },
    } 

ids=list(product.keys())


print("This is the curent inventory")
print("ID             name        price       quantity")
for id, product_details in product.items():
    name = product_details["name"]
    price = product_details["price"]
    quantity = product_details["quantity"]
    print(f"{id}        {name}          {price}             {quantity}")