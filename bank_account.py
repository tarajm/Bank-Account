class BankAccount:
    accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate , balance): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    
    
    
    #increases the account balance by the given amount
    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self



    def withdraw(self, amount):
        # your code here
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        # your code here
        print(self.balance)
        return self

#increases the account balance by the current balance * the interest rate 
# (as long as the balance is positive)
    def yield_interest(self):
        # your code here
        if self.balance >= 0:
            self.balance += (self.balance *self.int_rate)
        return self

    @classmethod    
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

##1st Account
tara_bank_account1 = BankAccount(.01, 50)
# tara_bank_account1.display_account_info()
# tara_bank_account1.deposit(50)
# tara_bank_account1.deposit(50)
# tara_bank_account1.deposit(50)
# tara_bank_account1.display_account_info()
# tara_bank_account1.withdraw(201)
# tara_bank_account1.display_account_info()
# tara_bank_account1.yield_interest()
# tara_bank_account1.display_account_info()
#chaining method
tara_bank_account1.deposit(50).deposit(50).deposit(50).withdraw(201).yield_interest().display_account_info()

##2nd Account
tara_bank_account2 = BankAccount(.05, 25000)
tara_bank_account2.deposit(25000).deposit(25000).withdraw(10000).withdraw(10000).withdraw(10000).withdraw(10000).yield_interest().display_account_info()

BankAccount.print_all_accounts()