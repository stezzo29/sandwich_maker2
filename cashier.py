

class Cashier:
    def process_coins(self):
        print("Please insert coins.")
        total = int(input("How many quarters? ")) * 0.25
        total += int(input("How many dimes? ")) * 0.10
        total += int(input("How many nickels? ")) * 0.05
        total += int(input("How many pennies? ")) * 0.01
        return total

    def transaction_result(self, money_received, sandwich_cost):
        if money_received >= sandwich_cost:
            change = round(money_received - sandwich_cost, 2)
            print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False
