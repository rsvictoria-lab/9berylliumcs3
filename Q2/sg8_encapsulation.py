class BankAccount:  
  def __init__(self, accNum, initial_balance):  
    self.__account_number = accNum
    self.__balance = initial_balance

  def set_account_number(self, accNum):
    self.__account_number = accNum

  def set_balance(self, newbalance):
    print(f"Update balance to {newbalance}")
