from utils import *

# UI -- helper

PLASTIC_TYPES = {
        1 : "PET", 
        2 : "HDPE",
        3 : "PVC",
        4 : "LDPE",
        5 : "PP",
        6 : "PS",
        7 : "OTHER"
        }

def item_sorted():
    print("\n Available plastic type: ") 

    for number, plastic in PLASTIC_TYPES.items():
        print(f"{number}. {plastic}")

def get_plastic_type():

    choice = get_int_input("\nChoose plastic type (1-7): ", 1, 7)
    if choice in PLASTIC_TYPES:
        return PLASTIC_TYPES[choice]
