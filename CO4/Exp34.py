class Bank:
    def __init__(self, accnum, name, type, bal):
        self.accnum = accnum
        self.name = name
        self.type = type
        self.bal = bal
    def deposit(self, amount):
        self.bal = self.bal + amount
        print("Amount deposited successfully")
        return self.bal
    def withdraw(self, amount):
        if amount > self.bal:
            print("Insufficient balance")
            return self.bal
        else:
            self.bal = self.bal - amount
            print("Amount withdrawed successfully")
            return self.bal
b = Bank(12045,"Nihala","savings",5000)
damount = float(input("Enter the amount to be deposited: "))
print("Your Account balance is:", b.deposit(damount))
wamount = float(input("Enter the amount to be withdrawn: "))
print("Your Account balance is:", b.withdraw(wamount))
