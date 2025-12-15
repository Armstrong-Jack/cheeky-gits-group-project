product =  {
    101:  {"name": "Laptop", "price": 99.99, "quantity": 20},
    102: {"name": "PC", "price": 200, "quantity": 10},
    } 
ids = list(product.keys())
print(ids)


while True:
    user_choice = input("would you like to add(a) or remove(r) a product. or would you like to go back to menu(q)")
    new_product = {}


    if user_choice == "a":
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


        product[ids[len(ids)-1]+1] = new_product
        print(new_product)
        print(product)
        
            
    elif user_choice == "r":
        print("you have selected to remove a file")

        while True: 
            try:
                entered_product_id = int(input("please enter the id of the item you want to remove"))
                break
            except ValueError:
                print("you have entered the wrong value. it needs to be numbers")
            
        for id in ids:
            if id == entered_product_id:
                id_to_remove = id
                index_of_element_to_remove = ids.index(id_to_remove)
                product.pop(id_to_remove)
                ids.pop(index_of_element_to_remove)
                print(ids)
                print(product)
            else:
                print("you have entered an incorrect id")

    elif user_choice == "q":
        print("you have selected to return to the menu")
    else:
        print("you have selected an incorrect option please try again")