import os

class Product:
    '''
    This class represents a product to be added in a shopping cart.

    Attributes:
        name (string) - the name of the product
        price (double) - the price of the product
        quantity (integer) - the quantity of the product

    Methods:
        get_name - returns the name of the product
        get_price - returns the rounded price of the product
        get_quantity - returns the quantity of the product

    '''
    # NOTE: added new attribute 'quantity'
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - \u20b1{round(self.price, 2)} x{self.quantity}"
    
    # NOTE: added accessor functions
    def get_name(self):
        return self.name
    
    def get_price(self):
        return round(self.price, 2)
    
    def get_quantity(self):
        return self.quantity

class ShoppingCart:
    '''
    This class represents a shopping cart that you can add, view, and purchase products,

    Attributes:
        user_balance (double) - the current balance of the user
        products (list) - the list of all the products 

    Methods:
        add_product - adds a product to the list of products
        list_products - displays all the products in the list
        purchase_product - purchase from the list of products
        get_user_balance - returns the current balance
        get_list_length - returns the number of items in the cart
        increase_balance - adds additional balance to the current balance
    
    '''
    def __init__(self, balance):
        self.user_balance = balance
        self.products = []

    def add_product(self, product):
        '''
        Adds a product to the list of products.

        Parameters:
            product (object) - instance of the Product class

        '''
        self.products.append(product)

    def list_products(self):
        if self.get_list_length() == 0:
            print("No items. Please add to cart first.")
        else:
            for i in range(self.get_list_length()):
                print(f"{i+1}. {self.products[i]}")

    def purchase_product(self, index):
        '''
        Purchase from the list of products.

        Parameters:
            index (integer) - the number of the product in the list 

        '''
        name = self.products[index].get_name()
        quantity = self.products[index].get_quantity()
        price = self.products[index].get_price()
        total = quantity * price

        if self.user_balance < total: 
            print("\nInsufficient balance!")
            return 0

        print(f"\nPurchased \'{name}\' x{quantity} for \u20b1{price} each.")
        print("\nItem total: \u20b1", total)

        self.user_balance -= total
        print("\nYour new balance is: \u20b1", self.get_user_balance())

        self.products.pop(index)

    # NOTE: New functions added
    def get_user_balance(self):
        return round(self.user_balance, 2)
    
    def get_list_length(self):
        return len(self.products) if self.products is not None else 0
    
    def increase_balance(self, added_balance):
        '''
        Adds additional balance to the current balance.

        Parameters:
            added_balance (double) - balance added to the current balance
        
        '''
        self.user_balance += added_balance


# NOTE: new function added for convenience
def display(message_type):
    match (message_type):
        case "menu":
            print("\n1) Add Product")
            print("2) List Products")
            print("3) Purchase Product")
            print("4) Check Balance")
            print("5) Add balance")
            print("6) Exit")
            
        case "welcome message":
            print("Welcome to PyShop! Where shopping is your only way to get your money back!")

        case "wait message":
            input("\nPress enter to continue...")

        case "error message #1":
            print("\nPlease enter a valid balance!")
            input("\nPress enter to continue...")

        case "error message #2":
            print("\nInput not in the choices!")
            input("\nPress enter to continue...")

        case "error message #3":
            print("\nPrice must be a positive number!")

        case "error message #4":
            print("\nQuantity must be a positive integer!")

# NOTE: new function added to validate input for adding balance
def add_balance():
    while 1:
        try: 
            new_balance = float(input("\nEnter additional balance: \u20b1"))
            
            if new_balance < 1: raise ValueError

            break

        except ValueError:
            display("error message #1")

    cart.increase_balance(new_balance)

    print("\nAdditional balance added.\n\nYour new balance is: \u20b1", cart.get_user_balance())


if __name__ == "__main__":
    # Reapeat until user choose to exit
    while 1:
        
        os.system('cls') # clear the screen output

        display('welcome message')

        try: 
            balance = float(input("\nEnter your initial balance: \u20b1"))
            
            if balance < 1: raise(ValueError)

            cart = ShoppingCart(balance)

            # NOTE: Default items to cart added by the developer
            cart.add_product(Product("HP Laptop", 53999.99, 5))

            while 1:
                os.system('cls') 
                display("welcome message")

                display("menu")

                try:
                    choice = int(input("\nEnter the number of your choice: "))
                    
                    match(choice):
                        # Adding new product to cart
                        case 1:
                            product_name = input("\nEnter product name: ")
                            while 1:
                                try:
                                    product_price = float(input("\nEnter product price: \u20b1"))

                                    if product_price < 1: raise ValueError
                                    
                                    while 1:
                                        try:
                                            quantity = int(input("\nEnter quantity: "))

                                            if quantity < 1: raise ValueError
                                            break
                                        except ValueError:
                                            display("error message #4")
                                    
                                    new_product = Product(product_name, product_price, quantity)

                                    cart.add_product(new_product)

                                    print("\nAdded product: ", new_product)

                                    display("wait message")

                                    break
                                except ValueError:
                                    display("error message #3")

                        # Displaying list of products in cart
                        case 2:
                            os.system('cls')

                            print("Products in the cart:")
                            cart.list_products()

                            display("wait message")

                        # Purchasing a product
                        case 3:
                            while 1:
                                os.system('cls')
                                print("Purchasing a product...\n")
                                cart.list_products()

                                # Stops the purchase if there is no product in the cart
                                if cart.get_list_length() < 1: 
                                    display("wait message")
                                    break

                                try:
                                    index = int(input("\nEnter the product number to purchase: "))
                                    
                                    # raise an error if the input is not in the list
                                    if index not in range(1, cart.get_list_length()+1): raise ValueError
                                    
                                    # proceed to ask user for additional balance if the function returns a value
                                    if cart.purchase_product(index-1) is not None:
                                        display("wait message")

                                        while 1:
                                            os.system('cls')

                                            choice = input("Would you like to add balance? (y/n): ")
                                            
                                            match(choice):
                                                case 'y':  
                                                    add_balance()
                                                    break
                                                
                                                case 'n': 
                                                    print("\nPlease add a balance if you want to purchase selected product.")
                                                    break

                                                case _: display("error message #2")
                                    
                                    display("wait message")
                                    break
                                
                                except ValueError: 
                                    display("error message #2")

                        # Display current balance
                        case 4:
                            os.system('cls')
                            
                            print("\nYour current balance is: \u20b1", cart.get_user_balance())

                            display("wait message")

                        # Add balance
                        case 5: 
                            add_balance()
                            display("wait message")

                        # Exits program
                        case 6: break

                        case _: raise ValueError

                except ValueError:
                    display("error message #2")
        
            break

        except ValueError:
            display("error message #1")