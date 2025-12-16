product =  {
    101:  {"name": "Laptop", "price": 99.99, "quantity": 20},
    102: {"name": "PC", "price": 200, "quantity": 3},
    103: {"name": "keyboard", "price":200 , "quantity": 200},
    104: {"name": "Mouse" , "price":100 , "quantity":200 },
    105: {"name": "speakers", "price":100 , "quantity":200 },
    106: {"name":"HEadphones" , "price":100 , "quantity":200 },
    107: {"name": "Xbox Controller", "price":100 , "quantity":200 },
    108: {"name":"PS4 Controller" , "price":100 , "quantity":200 },
    } 

low_quantity_product_names = []
low_quantity_product_id = []
BELOW_LOW_STOCK_FRESHHOLD = 5
for id, product_details in product.items():
    if product_details["quantity"] <= BELOW_LOW_STOCK_FRESHHOLD:
        low_quantity_product_names.append(product_details["name"])
        low_quantity_product_id.append(id)
        current_product_name = product_details["name"]
        print(f"this item: {current_product_name} \n with the ID: {id}")


