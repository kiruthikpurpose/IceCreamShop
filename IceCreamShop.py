class IceCream:
    def __init__(self, flavor, price):
        self.flavor = flavor
        self.price = price

class IceCreamShop:
    def __init__(self):
        self.menu = []
        self.total_sales = 0
    
    def add_flavor(self, flavor, price):
        ice_cream = IceCream(flavor, price)
        self.menu.append(ice_cream)
    
    def list_menu(self):
        print("Welcome to our Ice Cream Shop! Here's our menu:")
        for index, ice_cream in enumerate(self.menu, start=1):
            print(f"{index}. {ice_cream.flavor} - ${ice_cream.price}")
    
    def order(self, flavor_index):
        selected_flavor = self.menu[flavor_index - 1]
        print(f"You ordered {selected_flavor.flavor} ice cream.")
        self.total_sales += selected_flavor.price
    
    def display_sales(self):
        print(f"Total Sales: ${self.total_sales}")

# Example usage:
if __name__ == "__main__":
    shop = IceCreamShop()
    
    # Adding flavors to the menu
    shop.add_flavor("Vanilla", 3.0)
    shop.add_flavor("Chocolate", 3.5)
    shop.add_flavor("Strawberry", 4.0)
    
    # Displaying the menu
    shop.list_menu()
    
    # Placing orders
    shop.order(1)  # Order Vanilla
    shop.order(2)  # Order Chocolate
    shop.order(3)  # Order Strawberry
    
    # Displaying total sales
    shop.display_sales()
