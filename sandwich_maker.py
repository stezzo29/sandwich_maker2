
class SandwichMaker:
    def __init__(self, resources):
        self.resources = resources

    def check_resources(self, sandwich_type, recipes):
        for ingredient in recipes[sandwich_type]:
            if recipes[sandwich_type][ingredient] > self.resources.get(ingredient, 0):
                print(f"Sorry, there is not enough {ingredient}.")
                return False
        return True

    def make_sandwich(self, sandwich_type, recipes):
        if self.check_resources(sandwich_type, recipes):
            for ingredient in recipes[sandwich_type]:
                self.resources[ingredient] -= recipes[sandwich_type][ingredient]
            print(f"{sandwich_type} is ready!")
        else:
            print("Cannot make the sandwich.")
