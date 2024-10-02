

import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

def main():
    resources = data.resources
    recipes = data.recipes
    sandwich_maker = SandwichMaker(resources)
    cashier = Cashier()

    is_on = True

    while is_on:
        choice = input("What would you like? (Ham Sandwich) or type 'off' to exit: ").lower()
        
        if choice == 'off':
            is_on = False
        elif choice == 'ham sandwich':
            sandwich_cost = 5.0  # Define cost for the sandwich
            
            if sandwich_maker.check_resources("Ham Sandwich", recipes):
                print(f"The cost is ${sandwich_cost}.")
                money_received = cashier.process_coins()
                
                if cashier.transaction_result(money_received, sandwich_cost):
                    sandwich_maker.make_sandwich("Ham Sandwich", recipes)
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
