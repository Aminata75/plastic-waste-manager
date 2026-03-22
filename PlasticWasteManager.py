from datetime import datetime
import json
from utils import *
from UI_helper import *


DATA_FILE = "inventory.json"
GRAMS_PER_ML = 0.025
KG_PER_GRAM = 1000
CO2_PER_KG = 2
width = 100

class PlasticItem:
# PlasticItem handles item behavior
    def __init__(self, item_id, plastic_type, quantity, size, sort_date, timestamp=None):
        self.id = item_id
        self.plastic_type = plastic_type
        self.quantity = quantity
        self.size = size
        self.sort_date = sort_date
        self.timestamp = timestamp if timestamp else datetime.now()
    
# INSTANCE METHOD
    def to_dict(self):
        return {
            "item_id" : self.id,
            "plastic_type" : self.plastic_type,
            "quantity" : self.quantity,
            "size" : self.size,
            "sort_date" : self.sort_date.strftime("%Y-%m-%d"),
            "timestamp" : self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        }
        
    def description(self):
        return f"{self.plastic_type} - {self.size}ml sorted on {self.sort_date.strftime('%Y-%m-%d')}"

    def size_category(self):
        return PlasticItem.size_group(self.size)
        
    def recyclability(self):
        level, symbol = PlasticItem.recyclability_level(self.plastic_type)
        return f"{symbol} {level}"
    

# CLASS METHOD
    @classmethod
    def create_item(cls, item_id, plastic_type, quantity, size, sort_date, timestamp):
        return cls(item_id, plastic_type, quantity, size, sort_date, timestamp)
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["item_id"],
            data["plastic_type"],
            data["quantity"],
            data["size"],
            datetime.strptime(data["sort_date"],"%Y-%m-%d"),
            datetime.strptime(data["timestamp"], "%Y-%m-%d %H:%M:%S")
        )

# STATIC METHODS
    @staticmethod
    def is_valid_size(size):
        return size > 0
    
    @staticmethod
    def size_group(size):

        if size < 300:
            return "Small"
        elif size <= 700:
            return "Medium"
        else:
            return "Large"
    
    @staticmethod
    def recyclability_level(plastic_type): 
        # This fits perfectly as a static method, because it simply returns information based on input
        # This is a property of the plastic type
        levels = {
            "PET" : ("High", "🟢"),
            "HDPE" : ("High", "🟢"),
            "LDPE" : ("Medium", "🟠"),
            "PP" : ("Medium", "🟠"),
            "PVC" : ("Low", "🔴"),
            "PS" : ("Low", "🔴"),
            "OTHER" : ("Low", "🔴"),
        }

        return levels.get(plastic_type, ("Unknown", "⚪️"))

# DUNDER METHOD
    def __str__(self):
        return f"{self.id} | {self.plastic_type} | {self.size}ml"

# DEBUG DUNDER METHOD
    def __repr__(self):
        return f"PlasticItem(id={self.id}, type={self.plastic_type}, size={self.size})"





class PlasticWasteManager: 
    # PlasticWasteManager handles inventory behavior
    def __init__(self):
        self.inventory = {}
        self.item_id = 1 
        self.load_inventory()

# INSTANCE METHOD
    def total_items(self):
        
        total = 0

        for item in self.inventory.values():
            total += item.quantity

        return total
    
    def add_item(self, plastic_type, size, sort_date):
        quantity = 1         
        item = PlasticItem(
            self.item_id, 
            plastic_type, 
            quantity, 
            size, 
            sort_date
        )
        
        self.inventory[self.item_id] = item 
        self.item_id += 1 

        print(f"{quantity} {plastic_type} of {size}ml added to inventory.")
        
        self.save_inventory()

        return item 

    def save_inventory(self):

        data = []

        for item in self.inventory.values():
            data.append(item.to_dict())

        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)

    def load_inventory(self):

        self.inventory ={}
        
        try:
            with open(DATA_FILE, "r") as file:
                data = json.load(file)

            for item_data in data:
                item = PlasticItem.from_dict(item_data)
                self.inventory[item.id] = item

                if item.id >= self.item_id:
                    self.item_id = item.id + 1

        except FileNotFoundError:
            pass

    def get_item(self, item_id: int):
        return self.inventory.get(item_id)

        # item = self.inventory.get(item_id)

        # if item:
        #     print("=" * 100)
        #     print(f"{'ID':<5}{'TYPE':<10}{'QTY':<10}{'SIZE':<10}{'RECYCLABLE':<15}{'SORT DATE':<15}")
        #     print("=" * 100)
        #     print(
        #         f"{item.id:<5}"
        #         f"{item.plastic_type:<10}"
        #         f"{item.quantity:<10}"
        #         f"{str(item.size) + 'ml':<10}"
        #         f"{item.recyclability():<15}"
        #         f"{item.sort_date.strftime('%Y-%m-%d'):<15}"
        #     )

        # else:
        #     print("Item not found.")

        # print("=" * 100)

    def update_item(self, item_id, plastic_type=None, size=None, sort_date=None):

        item = self.inventory.get(item_id)

        if not item:
            return None
        
        if plastic_type:
            item.plastic_type = plastic_type

        if size is not None:
            item.size = size
        
        if sort_date:
            item.sort_date = sort_date

        return item
        # if not item:
        #     print("Item not found!")


        # print(f"Type --> ({item.plastic_type}).")
        # item_sorted()
        # new_type = get_plastic_type()
        # if new_type:
        #     item.plastic_type = new_type

        # new_size = get_int_input(f"Size ({item.size}ml): ")
        # if new_size:
        #     item.size = new_size

        # new_date = date_input(f"Date ({item.sort_date}): ")
        # if new_date:
        #     item.sort_date = new_date

        # print("Item updated successfully!")

        self.save_inventory()

    def remove_item(self, item_id):

        if item_id in self.inventory:
            del self.inventory[item_id]
            self.save_inventory()
            print(f"Item with id number: {item_id} removed.")
            

        else:
            print("Item not found in inventory.")   

    def plastic_type_totals(self):

        totals = {}

        for item in self.inventory.values():
            plastic = item.plastic_type

            if plastic not in totals:
                totals[plastic] = 0

            totals[plastic] += item.quantity

        return totals

    def plastics_size_totals(self):

        size_totals = 0

        for item in self.inventory.values():
            
            size_totals += item.size * item.quantity
        
        return size_totals

    def size_summary(self):

        category = {
            "Small": 0,
            "Medium": 0,
            "Large": 0
        }

        for item in self.inventory.values():
            size_level = PlasticItem.size_group(item.size)

            if size_level in category: 
                category[size_level] += item.quantity

        return category

    def average_size(self):
        size_total = self.plastics_size_totals()
        total = self.total_items()
        

        for item in self.inventory.values():
            if self.total_items == 0:
                return 0
            
        return size_total / total

    def recyclability_summary(self):

        summary = {
            "🟢 High": 0,
            "🟠 Medium": 0,
            "🔴 Low": 0
        }

        for item in self.inventory.values():

            level, symbol = PlasticItem.recyclability_level(item.plastic_type)

            key = f"{symbol} {level}"

            if key in summary:
                summary[key] += item.quantity

        return summary

    def environmental_stats(self):
    # 1 liter (1000 ml) ≈ 25 grams of plastics
    # weight (grams) = size_ml x 0.025
    # convert to kg -- grams / 1000
    # 1 kg recycled plastic ≈ 2 kg CO2
        total_weight = self.plastics_size_totals()
        weight_kg = (total_weight * GRAMS_PER_ML) / KG_PER_GRAM
        co2_saved = weight_kg * CO2_PER_KG

        if self.total_items() == 0:
            return {
                "total_weight": 0,
                "co2-saved": 0
            }
        
        return {
            "total_weight": f"{round(weight_kg, 2)} kg",
            "co2_saved": f"{round(co2_saved, 2)} kg"
        }
    
    def display_inventory(self):

        if not self.inventory:
            print("\nInventory is empty.")
            return

        print("\n" + "=" * width)
        print("CURRENT INVENTORY".center(width))
        print("=" * width)
        print(f"{'ID':<5}{'TYPE':<10}{'QTY':<10}{'SIZE':<10}{'RECYCLABLE':<15}{'SORT DATE':<15}{'Day & Time':<20}")        
        print("-" * width)

        for item in self.inventory.values():
            print(
                f"{item.id:<5}"
                f"{item.plastic_type:<10}"
                f"{item.quantity:<10}"
                f"{str(item.size) + 'ml':<10}"
                f"{item.recyclability():<15}"
                f"{item.sort_date.strftime('%Y-%m-%d'):<15}"
                f"{item.timestamp.strftime('%Y-%m-%d %H:%M:%S'):<20}"
            )

        print("=" * width)

    def search_by_date(self, start_date, end_date):
        
        results = []
        
        for item in self.inventory.values():

            if start_date > end_date:
                print("Swapping dates..")
                start_date, end_date = end_date, start_date

            if start_date <= item.sort_date <= end_date :
                results.append(item)

        if not results:
                print("item not found in this range!")
                return
        
        print("=" * width)
        print("SEARCH BY DATE".center(width))
        print(f"{'ID':<5}{'TYPE':<10}{'QTY':<10}{'SIZE':<10}{'DATE':<15}")
        print("-" * width)

        for item in results:
            print(
                f"{item.id:<5}"
                f"{item.plastic_type:<10}"
                f"{item.quantity:<10}"
                f"{str(item.size) + 'ml':<10}"
                f"{item.sort_date.strftime('%Y-%m-%d'):<15}"
            )
        
        print("-" * width)
    
    def get_statistics(self):

        return {
            "total_items": self.total_items(),
            "plastic_type" : self.plastic_type_totals(),
            "plastics_size" : self.plastics_size_totals(),
            "size_summary" : self.size_summary(),
            "avg_size" : self.average_size(),
            "recycle_summary" : self.recyclability_summary(),
            "environment" : self.environmental_stats()
        }

    def display_statistics(self):

        print("\n" + "=" * width)
        print("INVENTORY STATISTICS".center(width))
        print("=" * width)

        print(f"\nTotal items: {self.total_items()}")

        print(f"\nPlastic type Totals:")
        totals = self.plastic_type_totals()
        for plastic, count in totals.items():
            print(f"{plastic:<10}: {count}")

        print(f"\nTotal size: {self.plastics_size_totals()} ml")
        
        print(f"\nSize Summary:")
        category = self.size_summary()
        for size, count in category.items():
            print(f"{size:<10}: {count}")

        print(f"\nAverage size: {self.average_size():.2f} ml")

        print(f"\nRecyclability Summary:")
        summary = self.recyclability_summary()
        for plastic, count in summary.items():
            print(f"{plastic:<10}: {count}")

        print(f"\nEnvironmental impact:")
        print(self.environmental_stats())

        print("=" * width)

# CLASS METHOD
    # Class methods operate on the class itself, not a specific manager instance
    @classmethod
    def empty_manager(cls):
        return cls()

# STATIC METHOD
    @staticmethod
    def is_valid_plastic_type(plastic_type):
        valid = ["PET", "HDPE", "PVC", "LDPE", "PP", "PS", "OTHER"]
        return plastic_type in valid
    
# DUNDER METHOD
    def __len__(self): # It allows python to treat Manager as a container
        print(len(self.inventory))

# DUNDER METHOD
    def __str__(self): 
        return f"PlasticWasteManager with {len(self.inventory)} items"
 
