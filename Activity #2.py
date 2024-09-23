import os 

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - \u20b1{self.price}"

class ShoppingCart:
    
    def __init__(self, balance):
        self.user_balance = balance
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        for i in range(len(self.products)):
            print(f"{i+1}. {self.products[i]}")

    def purchase_product(index):
        pass

def open_menu():
    os.system('cls')
    print("Welcome to PyShop!")
    
    balance = 1000000

    cart = ShoppingCart(balance)

    prod1 = Product("Keyboard", 500)
    prod2 = Product("Mouse", 200)

    cart.add_product(prod1)
    cart.add_product(prod2)

    cart.list_products()

if __name__ == "__main__":
    open_menu()