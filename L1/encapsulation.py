# class BankAccount:
#     def __init__(self):
#         self.balance = 1000

# account = BankAccount()

# account.balance = -500   # Anyone can change it!
# print(account.balance)

# # With and capsulation
# class BankAccount:
#     def __init__(self):
#         self.__balance = 1000   # Private attribute

#     def deposit(self, amount):
#         self.__balance += amount

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Not enough money!")

#     def show_balance(self):
#         print("Balance:", self.__balance)


# account = BankAccount()

# account.deposit(500)
# account.withdraw(200)
# account.show_balance()

# print(account.__balance)\


class PiggyBank:
    def __init__(self):
        self.__money = 0

    def add_money(self, amount):
        self.__money += amount

    def show_money(self):
        print("Money: ", self.__money)

money = PiggyBank()

money.add_money(15)
money.add_money(20)
money.show_money()
        
