class product:
    def __init__(self, ID,):
        self.product_data = {"26628503": {"name": "Fanta", "price" : 1.5}}
        self.ID = ID
        self.name = self.product_data[ID]["name"]
        self.price = self.product_data[ID]["price"]

    def order(self, amount):

        cost = amount  * self.price
        return cost
    
    def add_product(self, new_id, new_name,new_price):
        self.product_data[new_id]= {"name": new_name, "price": new_price}
        


#print(product_data["26628503"]["name"])


IDs = ["26628503", "26628504", "26628505", "26628506", "26628507", "26618501", "26618502", "26618503", "26618504", "26618505"]
entered_ID = input("Enter the ID to search: ")
ID_search_length = len(entered_ID)
familler_ID =[]

for ID in IDs:
    ID2 = ID[0:ID_search_length]
    if entered_ID == ID2:
        familler_ID.append(ID)
        print(familler_ID)

for ID in familler_ID:
    print(f"{familler_ID.index(ID)}. {ID}")

choose_ID = int(input("Choose the index of the ID you want to select: "))
selected_ID = familler_ID[choose_ID]
print(f"You have selected ID: {selected_ID}")

prod = product(selected_ID)
print(prod.name)   
print(prod.order(int(input("how many woul you like to order"))))

choice = input("would you like to add product ID")
if choice == "y":
    ne = input("enter product name")
    id = input("product_id")
    pr = int(input("add the products price"))

    prod.add_product(id, ne, pr)
    
    print("succsesful here is the new list of products")
    print(prod.product_data)