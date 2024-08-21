class BankAccount:
    def __init__(self, acc_number, name, date) -> None:
        self.account_number = acc_number
        self.customer_name = name
        self.balance = 0
        self.date_of_opening = date

    # Phương thức tiền gửi
    def deposit(self, dp):
        if dp > 0:
            self.balance += dp
            print(f"Bạn đã gửi {dp} vào tài khoản {self.account_number}")
        else:
            print("Số tiền gửi phải lớn hơn 0")

    # Phương thức tiền rút
    def withdraw(self, wd):
        if wd > 0 and wd <= self.balance:
            self.balance -= wd
            print(f"Đã rút {wd} từ tài khoản {self.account_number}")
        else:
            print("Số tiền rút không hợp lệ")

    # Phương thức kiểm tra số dư
    def check_balance(self):
        print(f"Số dư hiện tại của tài khoản {self.account_number} là {self.balance}")

tk1 = BankAccount("0123456789", "Nam", "20/08/2024")
# tk1.deposit(10000000)
# print(tk1.balance)
# tk1.check_balance()
tk1.withdraw(200000)
tk1.check_balance()