import json

def load_data():
    #opens the file 
    try:
        with open("inventory.json", "r") as f:
            inventory_data = json.load(f)
            #if thier is no file it creates one
    except FileNotFoundError:
        print("Error: File Not found\n creating file\nNeed an item please create one below")
        with open("inventory.json", "w") as f:
            inventory = {}
            inventory_data= add_item(inventory)
            json.dump(inventory_data, f, indent= 4)
            print(inventory_data)

    product = {int(ids): product_details for ids, product_details in inventory_data.items()}

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
        


def add_remove_item(inventory):
    product = inventory

    ids = list(product.keys())
    while True:
        user_choice = input("would you like to add(a) or remove(r) a product. or would you like to go back to menu(q)")
        new_product = {}


        if user_choice == "a":
            product = add_item(product)
            return product

            
                
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
    ids = list(product.keys())
    print(ids)
    while True:
        user_choice = input("how would you like to search. by ID(1) or by Name(2) or price Range(3)")

        if user_choice == "1":


            for id in ids:
                while True:
                    try:
                        entered_id =int(input("please enter the products id"))
                        break
                    except ValueError:
                        print("entered wrong value. neededs to be number")
                if id == entered_id:
                    selected_id = id
                    print(f"your selected id is {selected_id}")
                    return selected_id

        elif user_choice == "2":

            entered_product_name = input("please enter the product name")

            for id, product_details in product.items():
                
                if product_details["name"] == entered_product_name:
                    selected_id = id
                    selected_product = product_details
                    print(f"you have selected this product{selected_product}")
                    return selected_id
        
        elif user_choice == "3":
            ids_in_price_range = []
            items_in_price_range = []
            items_prices = []
            user_options = []
            while True:
                while True:
                    try:
                        min_num = int(input("please Enter the smallest Number"))
                        max_num = int(input("please enter the largest number"))
                        if max_num >= min_num:
                            break
                        else:
                            print("please enter the nubers in correct order")
                    except ValueError:
                        print("please enter a correct value")
                
                for id, product_details in product.items():
                    if product_details["price"] <= max_num and product_details["price"] >= min_num:
                        ids_in_price_range.append(id)
                        product_name = product_details["name"]
                        product_price = product_details["price"]
                        items_in_price_range.append(product_name)
                        items_prices.append(product_price)
                        print(product_name, product_price)
                
                print(ids_in_price_range, items_in_price_range, items_prices)
                for i in range(len(ids_in_price_range)):
                    print(f"({i+1}).{ids_in_price_range[i]},  {items_in_price_range[i]},  £{items_prices[i]}")
                    user_options.append(i)
                
                if ids_in_price_range > []:
                    while True:
                        try:
                            user_choice = int(input("please enter the option you want"))
                            user_choice -= 1
                            break
                        except ValueError:
                            print("please enter a correct value")
                    if user_choice in user_options:
                        selected_id = ids_in_price_range[user_choice]
                        print(f"you have selected {selected_id}")
                        return selected_id
        else:
            print("wrong Value entered")


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


def generate_low_stock_report(inventory):
    product = inventory
    low_quantity_product_names = []
    low_quantity_product_id = []
    BELOW_LOW_STOCK_FRESHHOLD = 5
    for id, product_details in product.items():
        if product_details["quantity"] <= BELOW_LOW_STOCK_FRESHHOLD:
            low_quantity_product_names.append(product_details["name"])
            low_quantity_product_id.append(id)
            current_product_name = product_details["name"]
            print(f"this item: {current_product_name} \n with the ID: {id}")

def main():
    product = load_data()

    while True:

        print("1.View Stock \n2.Add/remove Item \n3.Update Item \n4.Search \n5.generate low quantity product list \nq for Quit ")
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
        
        elif choice == "5":
            generate_low_stock_report(product)

        elif choice == "q":
            print("you have chosen to Quit")
            break

        else:
            print("please enter a correct value")


if __name__ == "__main__":
    main()