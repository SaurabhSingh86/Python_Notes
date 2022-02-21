""" Banking """

# Part 1: =====>>>>


# class BankAccount:
#     def __init__(self, name, balance=0):
#         # instance variables => each customer will get a fresh copy of name, balance & transactions)
#         self.name = name
#         self.balance = balance
#         self.transactions = []
#         self.transactions.append(f'**** Initial Amount Deposited {balance} ****')
#
#     def deposit(self, amount):
#         self.balance += amount
#         self.transactions.append(f'Amount deposited {amount}')
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             raise ValueError("Insufficient Fund")
#         self.balance -= amount
#         self.transactions.append(f'Amount withdrawn {amount}')
#         return f'Kindly collect the cash {amount}'
#
#     def transfer(self, to_account, amount):
#         if amount > self.balance:
#             raise ValueError ("Insufficient Fund")
#         to_account.deposit(amount)
#         self.balance -= amount
#
#     def statement(self):
#         for transaction in self.transactions:
#             print(transaction)
#         print("*" * 20)
#         print(f'Available Balance in the Account {self.balance}')
#
#
# c1 = BankAccount("Saurabh", 1000)
# c2 = BankAccount("Gaurav")
#
# # print(c1.__dict__)
# # print(c2.__dict__)
#
# c1.deposit(10000)
# # print(c1.__dict__)
#
# c2.deposit(15000)
# # print(c2.deposit(15000))        # None
# # print(c2.__dict__)
#
# # c1.withdraw(5000)
# # print(c1.withdraw(5000))        # Kindly collect the cash 5000
# # print(c1.__dict__)
#
# # c1.withdraw(8000)               # ValueError: Insufficient Fund
#
#
# # c1.transfer(c2, 4000)
# # print(c1.__dict__)
#
# # c2.transfer(c1, 20000)           # ValueError: Insufficient Fund


# Part 2: ====>>> adding interest rate


# class BankAccount:
#     interest_rate = 0.04
#     # class variable => all the customers will share the same value or interest rate
#
#     def __init__(self, name, balance=0):
#         self.name = name
#         self.balance = balance
#         self.transactions = []
#         self.transactions.append(f'**** Initial Amount Deposited {balance} ****')
#
#     def deposit(self, amount):
#         self.balance += amount
#         self.transactions.append(f'Amount deposited {amount}')
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             raise ValueError("Insufficient Fund")
#         self.balance -= amount
#         self.transactions.append(f'Amount withdrawn {amount}')
#         return f'Kindly collect the cash {amount}'
#
#     def transfer(self, to_account, amount):
#         if amount > self.balance:
#             raise ValueError ("Insufficient Fund")
#         to_account.deposit(amount)
#         self.balance -= amount
#
#     def statement(self):
#         for transaction in self.transactions:
#             print(transaction)
#         print("*" * 20)
#         print(f'Available Balance in the Account {self.balance}')
#
#     def roi(self):
#         interest_amount = self.balance * BankAccount.interest_rate
#         # interest_amount = self.balance * self.__class__.interest_rate
#         self.balance += interest_amount
#         self.transactions.append(f'**** Interest Amount  credited *** {interest_amount}')
#
#
# c1 = BankAccount("Saurabh", 10000)
# c2 = BankAccount("Gaurav", 25000)
#
#
# c1.roi()
# print(c1.__dict__)


# ---------------------------------------------------------------------------------------------------------------------

""" Counting number of instances created to the class """

# example 1:

# class Demo:
#     count = 0                       # shared across all the instances
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         Demo.count += 1
#
#
# c1 = Demo(1, 2)
# print(Demo.count)       # 1
#
# c2 = Demo(5, 6)
# c3 = Demo(10, 2)
# c4 = Demo(2, 8)
# print(Demo.count)       # 4


# example 2: How many number of users access the login page


# class Access:
#     count_login_users = 0
#
#     def __init__(self, user_name, password):
#         self.user_name = user_name
#         self.password = password
#         Access.count_login_users += 1
#
#
# u1 = Access("Ss", 123)
# u2 = Access("Gs", 321)
# u3 = Access("Vs", 258)
# u4 = Access("Ps", 786)
# print(Access.count_login_users)             # 4


# ---------------------------------------------------------------------------------------------------------------------

""" Shopping Cart """

# Part 1: ====>>


# class ShoppingCart:
#     def __init__(self):
#         self.cart = []
#
#     def add_item(self, name, quantity, price):
#         self.cart.append({"name": name, "quantity": quantity, "price": price})
#
#     def total_cost(self):
#         total = 0                           # total = sum([item['quantity'] * item['price'] for item in self.cart])
#         for item in self.cart:
#             total += item["quantity"] * item["price"]
#         return total
#
#     def remove_item(self, name):
#         for item in self.cart:
#             if item['name'] == name:
#                 if item["quantity"] > 1:
#                     item['quantity'] -= 1
#                 else:
#                     self.cart.remove(item)
#
#
# c1 = ShoppingCart()
# c1.add_item("iphone", 2, 800)
# c1.add_item("imac", 1, 5000)
#
# print(c1.add_item.__dict__)


# Part 2: ====>>


class ShoppingCart:
    products = {"iphone": 5, "imac": 3, "ipad": 2, "iwatch": 4}
    prices = {"iphone": 900, "imac": 4500, "ipad": 5000, "iwatch": 3000}

    def __init__(self):
        self.cart = []

    def add_item(self, name, quantity):
        if name not in self.__class__.products:
            raise Exception("Product not available")
        elif self.__class__.products[name] >= quantity:
            self.cart.append({'name': name, 'price': self.__class__.prices[name]})
            self.__class__.products[name] -= quantity
        else:
            raise ValueError("Product out of stock")

    def total_cost(self):
        return sum([item['price'] * item['quantity'] for item in self.cart])

    def remove_item(self, name):
        for item in self.cart:
            if name == item["name"]:
                if item['quantity'] == 1:
                    self.cart.remove(item)
                else:
                    item['quantity'] -= 1

    # def summary(self):
