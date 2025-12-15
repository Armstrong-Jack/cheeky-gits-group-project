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
ids = list(product.keys())
print(ids)

def item_search(data_to_be_searched):
    product = data_to_be_searched
    ids =list(product.keys())
    user_choice = input("how would you like to search. by ID(1) or by Name(2)")

    if user_choice == "1":


        for id, product_details in product.items():
            while True:
                try:
                    entered_id =int(input("please enter the products id"))
                    break
                except ValueError:
                    print("entered wrong value. neededs to be number")
            if id == entered_id:
                selected_id = id
                selected_product = product_details
                print(f"your selected id is {selected_id}")
                return selected_id

    if user_choice == "2":

        entered_product_name = input("please enter the product name")

        for id, product_details in product.items():
            
            if product_details["name"] == entered_product_name:
                selected_id = id
                selected_product = product_details
                print(f"you have selected this product{selected_product}")
                return(selected_id)
            

selected_product_for_update = item_search(product)
print(selected_product_for_update)
print(product.keys(selected_product_for_update))


while True:
    user_choice = input("would you like to update the prodects quantity(1) or the products name(2) and finnally its price(3)")

    if user_choice == "1":
        print(selected_product_for_update)
        


        break
    elif user_choice == "2":
        print("f")

        break
    elif user_choice == "3":
        print("f")

        break
    else:
        print("wrong value entered please try again")
