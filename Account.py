#create a bank account class that has 2 attributes owner and balance.
#and 2 methods deposit and withdrawl.As an added requirement withdrawls
#may not exceed the available balance.
class Account():
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposit(self,deposit_amount):
        self.balance=self.balance+deposit_amount

    def withdrawl(self,withdrawl_amount):
        if self.balance>withdrawl_amount:
            self.balance = self.balance - withdrawl_amount
        else:
            print("Insufficient funds!")

    def __str__(self):
        return f'owner:{self.owner}\nBalance:{self.balance}'

a=Account("sam",500)
print(a)
a.deposit(500)
print(a)
a.withdrawl(600)
print(a)
a.withdrawl(1000)