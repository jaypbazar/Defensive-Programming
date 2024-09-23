import os

class Product:

    # NOTE: added new attribute 'quantity'
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - \u20b1{self.price}\tQuantity: {self.quantity}"

class ShoppingCart:
    
    def __init__(self, balance):
        self.user_balance = balance
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        if len(self.products) == 0:
            print("No items. Please add to cart first.")
        else:
            for i in range(len(self.products)):
                print(f"{i+1}. {self.products[i]}")

    def purchase_product(index):
        pass

    # NOTE: New functions added
    def increase_balance(self, added_balance):
        self.user_balance += added_balance

    def view_history(self):
        pass

def display(message_type):
    match (message_type):
        case "welcome message":
            print("Welcome to PyShop!")

        case "error message #1":
            print("\nPlease enter a valid balance!")
            input("\nPress enter to continue...")

        case "error message #2":
            print("\nInput not in the choices!")
            input("\nPress enter to continue...")

        case _:
            print("\nMessage type unknown!")

if __name__ == "__main__":
    # Reapeat until user choose to exit
    while 1:
        # clear the screen output
        os.system('cls')

        display('welcome message')

        try: 
            balance = int(input("\nEnter your initial balance: \u20b1"))
            
            if balance < 0: raise(ValueError)

            cart = ShoppingCart(balance)

            # NOTE: Default items to cart added by the developer
            cart.add_product(Product("Lenovo Laptop", 53000, 3))
            cart.add_product(Product("Asus Laptop", 60000, 2))

            while 1:
                os.system('cls')
                display("welcome message")

                print("\n1) Add Product")
                print("2) List Products")
                print("3) Purchase Product")
                print("4) Check Balance")
                print("5) Exit")

                try:
                    choice = int(input("\nEnter the number of your choice: "))
                    
                    if choice not in range(1, 5): raise ValueError

                    break
                except ValueError:
                    display("error message #2")

            break
        except ValueError:
            display("error message #1")