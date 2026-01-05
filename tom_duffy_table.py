product = {
    101: {"Name": "Laptop", "Price": 99.99, "Quantity": 20},
    102: {"Name": "PC", "Price": 200, "Quantity": 10},
    103: {"Name": "Keyboard", "Price": 200, "Quantity": 200},
    104: {"Name": "Mouse", "Price": 100, "Quantity": 200},
    105: {"Name": "Speakers", "Price": 100, "quantity": 200},
    106: {"Name": "Headphones", "Price": 100, "Quantity": 200},
    107: {"Name": "Xbox Controller", "Price": 100, "Quantity": 200},
    108: {"Name": "Ps4 Controller", "Price": 100, "Quantity": 200},
}

ids = list(product.keys())


print("This is the listed inventory currently")
print(" ID         Name            Price         Quantity")
for id, product_details in product.items():
    name = product_details["Name"]
    price = product_details["Price"]
    quantity = product_details["Quantity"]
    print(f"{id}      {name}           {price}            {quantity}")