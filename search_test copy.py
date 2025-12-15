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




def id_search_for_product(product_ids):
    ids = product_ids 

    while True:
        try:
            entered_ID = int(input("Enter the ID to search: "))
            break
        except ValueError:
            print("wrong value entered needs to be number")
    ID_search_length = len(entered_ID)
    familler_ID =[]
    amounts_of_similer_Ids = 0 
    for id in ids:
        id2 = id[0:ID_search_length]
        if entered_ID == id2:
            familler_ID.append(ID)
            amounts_of_similer_Ids += 1 

    if amounts_of_similer_Ids > 1:
        for ID in familler_ID:
            print(f"{familler_ID.index(ID)}. {ID}")
        choose_ID = int(input("Choose the index of the ID you want to select: "))
        selected_ID = familler_ID[choose_ID]
        print(f"You have selected ID: {selected_ID}")
        return selected_ID
    else:
        selected_ID = familler_ID
        print(f"You have selected ID: {selected_ID}")
        return selected_ID
    

print(id_search_for_product(ids))



        
