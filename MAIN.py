





def main():

    while True:

        print("1.View Stock \n2.Add Item \n3.Update Item \n4.Search \nq for Quit ")
        choice = input("PLease enter the option you want")

        if choice == "1":
            print("you have chose to view stock")

        elif choice == "2":
            print("you have chosen to Add item")

        elif choice == "3":
            print("you have chosen to Update item")

        elif choice == "4":
            print("you have chosen to Search")

        elif choice == "q":
            print("you have chosen to Quit")
            break

        else:
            print("please enter a correct value")


if __name__ == "__main__":
    main()