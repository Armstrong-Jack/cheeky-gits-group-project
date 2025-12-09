product =  {101:  { "Name": "Laptop", "price": 99.99, "quantity": 20}} 
ids = list(product.keys())
print(ids)

user_choice = input("how would you like to search. by ID(1) or by Name(2)")

if user_choice == "1":
    try:
        entered_id =int(input("please enter the products id")
        break
    except ValueError:
        print("entered wrong value. neededs to be number")

    for id in ids:
        if id == entered_id:
            selected_id = id
            print(f"your selected id is {selected_id})

if user_choice == "2":

        