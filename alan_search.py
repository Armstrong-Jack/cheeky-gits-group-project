
"""this is the ID and product name search task for Alan
DO NOT REMOVE OR CHANGE the structure for the dictionary below
your example piece is id_name_search_test.py"""
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

def item_search(inventory):
    product = inventory
    ids = list(product.keys())
    print(ids)

    while True:
        user_choice = input(
            "how would you like to search. by ID(1) or by Name(2) or price Range(3)"
        )

        if user_choice == "1":
            while True:
                try:
                    entered_id = int(input("please enter the products id"))
                    break
                except ValueError:
                    print("entered wrong value. neededs to be number")

            if entered_id in ids:
                selected_id = entered_id
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
                try:
                    min_num = int(input("please Enter the smallest Number"))
                    max_num = int(input("please enter the largest number"))
                    if max_num < min_num:
                        print("please enter the nubers in correct order")
                        continue
                    break
                except ValueError:
                    print("please enter a correct value")

            for id, product_details in product.items():
                if min_num <= product_details["price"] <= max_num:
                    ids_in_price_range.append(id)
                    items_in_price_range.append(product_details["name"])
                    items_prices.append(product_details["price"])
                    print(product_details["name"], product_details["price"])

            for i in range(len(ids_in_price_range)):
                print(f"({i+1}).{ids_in_price_range[i]},  {items_in_price_range[i]},  £{items_prices[i]}")
                user_options.append(i)

            if ids_in_price_range:
                while True:
                    try:
                        user_choice = int(input("please enter the option you want")) - 1
                        break
                    except ValueError:
                        print("please enter a correct value")

                if user_choice in user_options:
                    selected_id = ids_in_price_range[user_choice]
                    print(f"you have selected {selected_id}")
                    return selected_id

        else:
            print("wrong Value entered")
