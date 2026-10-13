class BankAccount:  
  def __init__(self, accNum, initial_balance):  
    self.__account_number = accNum
    self.__balance = initial_balance
  def set_account_number(self, accNum):
    self.__account_number = accNum
  def set_balance(self, newbalance):
    print(f"Update balance to {newbalance}")
    if newbalance < 0:
      print("Balance cant be negative. Balance remains the same.")
    else:
      self.__balance = newbalance
  def get_account_number(self):
    password = "password123"
    enterPassword = input("Enter password: ")
    if enterPassword == password:
      return self.__account_number
    else:
      print("Incorrect password")
      return None
  def get_balance(self):
    return self.__balance

accounts = []

my_account = BankAccount("12345", 1000)
accounts.append(my_account)

print(f"Account {len(accounts)}")
print(f"Account Number: {accounts[0].get_account_number()}")
print(f"Balance: {accounts[0].get_balance():.2f}")

my_account.set_balance(-100)

print()
print(f'Account {len(accounts)}')
print(f"Account Number: {accounts[0].get_account_number()}")
print(f"Balance: {accounts[0].get_balance():.2f}")
