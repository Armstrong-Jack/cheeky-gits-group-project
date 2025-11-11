
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

        
