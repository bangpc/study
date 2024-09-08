import pandas as pd

class Restaurant:
    def __init__(self):
        self.menu_items = pd.DataFrame(columns=['Món ăn', 'Giá'])
        self.book_table = pd.DataFrame(columns=['Tên khách hàng', 'Số lượng người', 'Thời gian'])
        self.customer_orders = pd.DataFrame(columns=['Tên khách hàng', 'Món ăn', 'Số lượng'])

    def add_item_to_menu(self, item, price):
        new_item = pd.DataFrame({'Món ăn': [item], 'Giá': [price]})
        self.menu_items = pd.concat([self.menu_items, new_item], ignore_index=True)

    def book_tables(self, name, num_people, time):
        new_booking = pd.DataFrame({'Tên khách hàng': [name], 'Số lượng người': [num_people], 'Thời gian': [time]})
        self.book_table = pd.concat([self.book_table, new_booking], ignore_index=True)

    def customer_order(self, name, item, quantity):
        new_order = pd.DataFrame({'Tên khách hàng': [name], 'Món ăn': [item], 'Số lượng': [quantity]})
        self.customer_orders = pd.concat([self.customer_orders, new_order], ignore_index=True)

    def print_menu(self):
        print(self.menu_items)

    def print_book_table(self):
        print(self.book_table)

    def print_customer_orders(self):
        print(self.customer_orders)

my_restaurant = Restaurant()

# Thêm các món ăn vào menu
my_restaurant.add_item_to_menu("Phở bò", 30000)
my_restaurant.add_item_to_menu("Bún chả", 35000)

# Đặt bàn
my_restaurant.book_tables("Nam", 4, "18h15")

# Đơn hàng
my_restaurant.customer_order("Nam", "Phở bò", 4)

# In menu, danh sách đặt bàn và đơn hàng
my_restaurant.print_menu()
my_restaurant.print_book_table()
my_restaurant.print_customer_orders()