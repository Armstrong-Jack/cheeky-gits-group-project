
"""this is the json save and load task for Jamie
DO NOT REMOVE OR CHANGE the structure for the dictionary below
your example piece is the def load and save functions in the MAIN.py"""
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

import json

#code imported from main.py for testing
def add_item(inventory):
    product = inventory
    ids = list(product.keys())
    new_product = {}



    print("you have selected to add a product")
            
    new_product["name"] = input("enter product name")

    while True:
            try:
                new_product["price"] = int(input("please enter the product's price"))
                break
            except ValueError:
                print("entered wrong value needs to be numbers")
            
    while True:
        try:
            new_product["quantity"] = int(input("please enter the product's quantity"))
            break
        except ValueError:
            print("entered wrong value needs to be numbers")

    try:
        product[ids[len(ids)-1]+1] = new_product
    except IndexError:
        product[101] = new_product
            
    print(new_product)
    print(product)
    return(product)

#load data function
def load_data():
    try:
        with open("inventory.json", "r") as f:
            inventory_data = json.load(f)
    #allows for alternate path if file is not found
    except FileNotFoundError:
        print("Error: File Not found\nCreating new file\nFile needs an item for the file, please create one")
        with open("inventory.json", "w") as f:
            inventory = {}
            #calls add item function if 'except' route runs
            inventory_data= add_item(inventory)
            json.dump(inventory_data, f, indent= 4)
            #prints the inventory
            print(inventory_data)
#save data function           
def save_inventory(sample):
    with open("inventory.json", "w") as fp:
        json.dump(sample, fp, indent=4)


#Alot of error handling done by me. see in test table and git commits!!!