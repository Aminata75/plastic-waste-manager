from datetime import datetime

# Input Validation

def date_input(prompt):

    while True:
        user_input = str(input(prompt))

        try:
            return datetime.strptime(user_input, "%Y-%m-%d")

        except ValueError:
                print("Invalid date format. Please enter a correct YYYY-MM-DD format.")  
                
def get_int_input(prompt, min_value=None, max_value=None): #DRY :)

    while True:
        try:
            value = int(input(prompt))

            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}")
                continue

            if max_value is not None and value > max_value:
                print(f"Value must be at most {max_value}")
                continue

            return value

        except ValueError:
            print("Please enter a valid number.")
   