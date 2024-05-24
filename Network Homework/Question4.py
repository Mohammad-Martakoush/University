


########################################
########## questions four ##############

class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. Current balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. Current balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Applied interest: ${interest:.2f}. New balance: ${self.balance:.2f}")

    def __str__(self):
        return f"Current balance: ${self.balance:.2f}, Interest rate: {self.interest_rate}%"

account = BankAccount("937893148", "Mohammad Martakoush")
account.deposit(1000) 
account.withdraw(500) 
print(f"Balance after withdrawal: ${account.get_balance():.2f}")  

savings_account = SavingsAccount("937893148", "Mohammad Martakoush", 7)
savings_account.deposit(1000)  
savings_account.apply_interest()  
print(savings_account) 




