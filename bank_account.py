class BankAccount:
    
    def __init__(self, int_rate=0.04, balance=0): 
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit Complete") 
        return self

    def withdraw(self, amount):
        if (self.balance - amount < 0):
            print("insufficient funds:Charging fee=$10.00")
        else:
            self.balance -= amount
        print("The remaining balance is:", self.balance)
        return self

    def display_account_info(self):
        print("The remaining balance is:", self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
          self.balance += self.balance * self.int_rate
        print(self.balance)
        print(self.int_rate)
        return(self)  

jake_bank_account = BankAccount(2600, 0.03)
dog_bank_account = BankAccount(3000, 0.05)

jake_bank_account.deposit(500).deposit(2000).deposit(5000).withdraw(200).yield_interest().display_account_info()
print("Jake's balance is:", jake_bank_account.balance)

dog_bank_account.deposit(500).deposit(500).withdraw(1000).withdraw(250).withdraw(150).withdraw(90).yield_interest().display_account_info()
print("Dog's balance is:", dog_bank_account.balance)


