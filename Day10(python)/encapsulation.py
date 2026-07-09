class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self._account_type = "savings"
        self.__balance =balance
    def deposite(self,amount):
        if amount >0:
           self.__balance+=amount
    def withdraw(self,amount):
        if 0<amount<=self.__balance:
            self.__balance-=amount
            print("withdraw successful")
        else:
            print("Insufficient balance or inavalid amount")
    def show_balance(self):
        print("Owner :",self.owner)
        print("Balance:",self.__balance)
account= BankAccount("Lahari",50000)

account.show_balance()
account.deposite(500)
account.withdraw(300)