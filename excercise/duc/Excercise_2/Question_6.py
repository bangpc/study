import pandas as pd

class Restaurant():
    def __init__(self) -> None:
        self.menu_items = pd.DataFrame(columns=['Item', 'Price'])
        self.book_table = pd.DataFrame(columns=['Number of table', 'Customer', 'Time'])
        self.customer_orders = pd.DataFrame(columns=['Customer', 'Item', 'Quality'])

    def add_item_to_menu(self):
        name = input("Input name of new item: ")
        price = input("Input price: ")
        self.menu_items.loc[len(self.menu_items)] = [name, price]
        print(f"Add {name} to menu with price {price}")

    def make_table_reservations(self):
        number = input("Input number of table: ")
        customer = input("Input customer: ")
        time = input("Input time: ")
        self.book_table.loc[len(self.book_table)] = [number, customer, time]
        print(f"Customer {customer} books table {number} at {time} successfully.")

    def take_customer_orders(self):
        customer = input("Input customer: ")
        item = input("Input item: ")
        quality = input(f"Input quality of {item}: ")
        self.customer_orders.loc[len(self.customer_orders)] = [customer, item, quality]
        print(f"Customer {customer} orders {item} with quality {quality}.")

    def print_menu(self):
        print("Menu Items:")
        print(self.menu_items)

    def print_table_reservations(self):
        print("Table Reservations:")
        print(self.book_table)

    def print_customer_orders(self):
        print("Customer Orders:")
        print(self.customer_orders)

def main():
    a = Restaurant()
    while True:
        print("\nChoose your option:\n1.Add item to menu.\n2.Make table reservations.\n3.Take customer orders.\n4.Print the menu.\n5.Print table reservations.\n6.Print customer orders.\n7.Exit.\nChoose 1/2/3/4/5/6/7")
        user_choice = input("\nEnter your option: ")

        if user_choice == '1':
            a.add_item_to_menu()

        elif user_choice == '2':
            a.make_table_reservations()

        elif user_choice == '3':
            a.take_customer_orders()

        elif user_choice == '4':
            a.print_menu()

        elif user_choice == '5':
            a.print_table_reservations()

        elif user_choice == '6':
            a.print_customer_orders()

        elif user_choice == '7':
            print("Exit the program.")
            break

        else:
            print("Invalid option.")

main()