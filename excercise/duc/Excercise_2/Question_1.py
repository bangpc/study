class BankAccount():
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
    
    def deposit(self, money):
        self.balance += money
        print(f"Deposited {money}. New balance is {self.balance}.")
        
    
    def withdraw(self, money):
        if self.balance >= money:
            self.balance -= money
            print(f"Withdrew {money}. New balance is {self.balance}.")
        else:
            print("Not enough balance")

    def check_balance(self):
        print(f"Account balance is: {self.balance}.")

acc1 = BankAccount("123456789", 1000000, "13/08/2024", "Le Anh Duc")
acc1.deposit(200000)
acc1.withdraw(200000)
acc1.withdraw(5000000)
acc1.check_balance()