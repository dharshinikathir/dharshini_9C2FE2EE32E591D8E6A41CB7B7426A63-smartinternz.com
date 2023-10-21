#challenge 2.1

class BankAccount:

  def __init__(self, accout_number,accout_holder_name,initial_balance=0.0):
    self._account_number = account_number
    self._account_holder_name = account_holder_name
    self._account_balance = initial_balance
    
  def deposit(self,amount):
    if amount > 0:
      self.__account_balance += amount
      print("Deposited ₹{}. New balance: ₹{}".format(amount, self.__account_balance))
    else:
      print("Invalid deposit amount. please deposit a positive amount.")
  
  def withdraw(self, amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      print("withdrew ₹{}. New balance: ₹{}".format(amount, self.__account_balance))
    else:
      print("Invalid withdrawal amount or insufficient balance.")
      
  def display_balance(self):
    print("Account balance for {} (account #{}): ₹{}".format(self.__account_holder_name, self.__account_number, self.__account_balance))


account = BankAccount (account_number="12345", account_holder_name="madhumitha", initial balance=500000.0)

account.display_balance()
account.deposit(5000.0)
account.withdraw(2000.0)
account.display_balance()