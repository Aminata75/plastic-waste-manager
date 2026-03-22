from datetime import datetime, timedelta
from PlasticWasteManager import PlasticWasteManager
from utils import *
from UI_helper import *


manager = PlasticWasteManager()
manager.load_inventory()

    
def display_menu():

    print("\n" + "=" *100)
    print("Plastic Waste Manager".center(100))
    print("=" * 100)
    print("1. ADD to inventory.")
    print("2. GET item.")
    print("3. UPDATE item.")
    print("4. REMOVE item.")
    print("5. Display INVENTORY.")
    print("6. Filter by date.")
    print("7. Display STATISTICS.")
    print("8. Exit")

def date_filter_menu():

    print("\nFilter by Date".upper())
    print("1. Today")
    print("2. Last 7 days")
    print("3. Custom range")

def filter_by_date(manager):

    while True:
        date_filter_menu()
        choice = get_int_input("Enter option (1-3): ", 1, 3)

        today = datetime.now()

        if choice == 1:
            start_date = today.replace(hour=0, minute=0, second=0)
            end_date = today
            manager.search_by_date(start_date,end_date)
            break


        elif choice == 2:
            start_date = today - timedelta(days=7)
            end_date = today
            manager.search_by_date(start_date,end_date)
            break


        elif choice == 3:
            start_date = date_input("Enter a start-date: ")
            end_date = date_input("Enter an end-date: ")
            manager.search_by_date(start_date, end_date)
            break

        else:
            print("Invalid choice. Try again!")


def main():

    print("\n Welcome to Plastic Waste Manager ".upper())
    while True:
        display_menu()
        choice = input("\n Enter your choice from (1 - 8): ")

        if choice == "1":
        
            item_sorted()
            plastic_type = get_plastic_type()
            size = get_int_input("Enter size in ml (e.g., 500ml): ", 1)
            sort_date = date_input("Enter a sort date: ")
            manager.add_item(plastic_type, size, sort_date)

        elif choice == "2":
             
            item_id = get_int_input("Enter item id: ", 1)
            manager.get_item(item_id)

        elif choice == "3":
            item_id = get_int_input("Enter item id: ", 1)
            manager.update_item(item_id)
                    
        elif choice == "4":
            item_id = get_int_input("Enter item id: ", 1)
            manager.remove_item(item_id)

        elif choice == "5":
            manager.display_inventory()

        elif choice == "6":
            filter_by_date(manager)

        elif choice == "7":
            manager.display_statistics()

        elif choice == "8":
            print("Exiting.")
            break

        else:
            print("Please enter a valid number.")
            

main()


                







    
        
        