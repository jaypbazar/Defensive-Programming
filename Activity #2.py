class Product:
    def __init__(self, name):
        self.name = name

    def __init__(self, name, price):
        self.name = name
        self.price = price

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
    pass

if __name__ == "__main__":
    open_menu()