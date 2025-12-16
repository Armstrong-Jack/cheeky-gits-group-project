import json

def load_data():
    #opens the file 
    try:
        with open("inventory.json", "r") as f:
            inventory_data = json.load(f)
            #if thier is no file it creates one
    except FileNotFoundError:
        print("Error: File Not found\n creating file")
        with open("inventory.json", "w") as f:
            inventory_data =json.dump([], f)

    product = {int(k): v for k, v in inventory_data.items()}

    #returns the data inside of the json file
    print(product)   
    return product



def save_inventory(sample):
    with open("inventory.json", "w") as fp:
        json.dump(sample, fp, indent=4)

def data_table(inventory):
    product = inventory
    ids=list(product.keys())


    print("This is the curent inventory")
    print("ID             name        price       quantity")
    for id, product_details in product.items():
        name = product_details["name"]
        price = product_details["price"]
        quantity = product_details["quantity"]
        print(f"{id}        {name}          {price}             {quantity}")


def add_remove_item(inventory):
    product = inventory

    ids = list(product.keys())



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
            return(product)
            
                
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
                    return product
                else:
                    print("you have entered an incorrect id")

        elif user_choice == "q":
            print("you have selected to return to the menu")
        else:
            print("you have selected an incorrect option please try again")

def item_search(inventory):
    product = inventory
   

    while True:
        user_choice = input("how would you like to search. by ID(1) or by Name(2)")
        if user_choice == "1":
            while True:
                    try:
                        entered_id =int(input("please enter the products id"))
                        break
                    except ValueError:
                        print("entered wrong value. neededs to be number")

            for id, product_details in product.items():
                
                if id == entered_id:
                    selected_id = id
                    selected_product = product_details
                    print(f"your selected id is {selected_id}")
                    return selected_id

        elif user_choice == "2":

            entered_product_name = input("please enter the product name")

            for id, product_details in product.items():
                
                if product_details["name"] == entered_product_name:
                    selected_id = id
                    selected_product = product_details
                    print(f"you have selected this product{selected_product}")
                    return(selected_id)
        else:
            print("wrong value entered")

def update_item(inventory):
    product = inventory 
    selected_product_for_update = int(item_search(product))
    print(selected_product_for_update)
    print(product[selected_product_for_update]["name"])


    while True:
        user_choice = input("would you like to update the prodects name(1) or the products price(2) and finnally its quantity(3)")

        if user_choice == "1":
            print(selected_product_for_update)
            product[selected_product_for_update]["name"] = input("enter product name")
            print(product[selected_product_for_update])
            return product 


        elif user_choice == "2":
            while True:
                try:
                    product[selected_product_for_update]["price"] = float(input("please enter the product's price"))
                    print(product[selected_product_for_update])
                    return product
                except ValueError:
                    print("entered wrong value needs to be numbers")

        elif user_choice == "3":
            while True:
                try:
                    product[selected_product_for_update]["quantity"] = int(input("please enter the product's quantity"))
                    print(product[selected_product_for_update])
                    return product
                except ValueError:
                    print("entered wrong value needs to be numbers")

        else:
            print("wrong value entered please try again")


def main():
    product = load_data()

    while True:

        print("1.View Stock \n2.Add/remove Item \n3.Update Item \n4.Search \nq for Quit ")
        choice = input("PLease enter the option you want")

        if choice == "1":
            print("you have chose to view stock")
            data_table(product)

        elif choice == "2":
            print("you have chosen to Add item")
            new_product_data = add_remove_item(product)
            save_inventory(new_product_data)

        elif choice == "3":
            print("you have chosen to Update item")
            new_product_data = update_item(product)
            save_inventory(new_product_data)

        elif choice == "4":
            print("you have chosen to Search")
            new_product_data = item_search(product)
            save_inventory(new_product_data)

        elif choice == "q":
            print("you have chosen to Quit")
            break

        else:
            print("please enter a correct value")


if __name__ == "__main__":
    main()