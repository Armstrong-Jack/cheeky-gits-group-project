product =  {101:  { "Name": "Laptop", "price": 99.99, "quantity": 20}} 
ids = list(product.keys())
print(ids)


while True:
    user_choice = input("would you like to add(a) or remove(r) a product. or would you like to go back to menu(q)")
    new_product = {}


    if user_choice == "a":
        print("you have selected to add a product")
        
        new_product["Name"] = input("enter product name")

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
        break
            
            












    elif user_choice == "r":
        print("you have selected to remove a file")
    elif user_choice == "q":
        print("you have selected to return to the menu")
    else:
        print("you have selected an incorrect option please try again")