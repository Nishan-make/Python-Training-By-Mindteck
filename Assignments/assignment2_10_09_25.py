# Scenario:
# You are building the backend logic of a product and order management system for an e-commerce platform like Amazon or Flipkart. The system needs to handle products, users, payments, discounts, and different order behaviors dynamically.
 
# Q1. Product Search System (Static Polymorphism) 
# Problem Statement:
# Implement a class ProductSearch that allows searching products with different combinations of criteria (name, category, price range).
# Requirements:
# Use default arguments and/or *args, **kwargs to simulate method overloading.
# Allow the following types of searches:
# Only by name
# Name and category
# Name, category, and price range
class ProductSearch:
    # using default/optional
    def search_products(self, name = None, category = None, price = None):
        if name and not category and not price:
            print(f"You have searched for {name}")
        elif name and category and not price:
            print(f"You have searched for {name}, which belongs to {category} category")
        elif name and category and price:
            print(f"You have searched for {name}, which belongs to {category}, and maximum price of {price}")
        else:
            print("Please provide something to search")

PrSearch = ProductSearch()
PrSearch.search_products("Paneer")
PrSearch.search_products("Mango", "Fruit")
PrSearch.search_products("Rice", "Food", 150)
PrSearch.search_products()
 
# Q2. Cart System with Quantity Variations (Static Polymorphism)
# Problem Statement:
# Design a class Cart that can add multiple products with variable quantities using *args or **kwargs. 
# Requirements: 
# Add multiple products at once with name and quantity
# Simulate static polymorphism using variable arguments

class Cart:
    def __init__(self):
        self.items = {}

    def add_to_cart(self, *args):
        for item in args:
            if isinstance(item, tuple) and len(item) == 2:
                name, quantity = item
                if name in self.items:
                    self.items[name] += quantity
                else:
                    self.items[name] = quantity
            else:
                print(f"Invalid item format: {item}")

 
# Q3. Discount Application (Static Polymorphism)
# Problem Statement:
# Create a class Discount that allows applying different types of discounts: 
# Flat discount 
# Percentage discount
# Buy One Get One
# Use static polymorphism to overload the method using default parameters or *args

class Discount:
    def apply(self, *args):
        if len(args) == 2 and isinstance(args[0], (int, float)) and isinstance(args[1], (int, float)):
            # Percentage discount: price, percentage
            price, percentage = args
            return price - (price * (percentage / 100))

        elif len(args) == 1 and isinstance(args[0], (int, float)):
            # Flat discount: fixed value
            return args[0] - 50  # assume flat $50 off

        elif len(args) == 3 and args[2] == 'bogo':
            # Buy One Get One: price, quantity, 'bogo'
            price, quantity, _ = args
            paid_items = (quantity // 2) + (quantity % 2)
            return paid_items * price

        else:
            raise ValueError("Invalid discount arguments.")


d = Discount()

print(d.apply(500))  # flat discount
print(d.apply(500, 10))  # percentage discount
print(d.apply(100, 3, 'bogo'))  # BOGO: Buy 1 Get 1

 
 
# Q4. Payment System (Dynamic Polymorphism)
# Problem Statement:
# Implement a base class Payment and subclasses CreditCardPayment, UPIPayment, and CODPayment. Each should override a method pay().
# Requirements:
# Override pay() method in each class to simulate different payment methods

class Payment:
    def pay(self, amount):
        raise NotImplementedError("Subclasses must override this method.")

class CreditCardPayment(Payment):
    def pay(self, amount):
        return f"Paid ${amount} using Credit Card."

class UPIPayment(Payment):
    def pay(self, amount):
        return f"Paid ${amount} using UPI."

class CODPayment(Payment):
    def pay(self, amount):
        return f"Payment of ${amount} will be made upon delivery."


# Examples
payment_method = CreditCardPayment()
print(payment_method.pay(1000))

payment_method = UPIPayment()
print(payment_method.pay(500))

payment_method = CODPayment()
print(payment_method.pay(250))