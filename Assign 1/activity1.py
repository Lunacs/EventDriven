import time

class MyBank:
    def __init__(self):
        self.balance = 0.0

    def check_balance(self):
        print(f"Current balance: ₱{self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print(f"You deposited ₱{amount:.2f}!")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"You withdrew ₱{amount:.2f}!")


if __name__ == '__main__':
    account = MyBank()
    while True:
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            account.check_balance()
            time.sleep(1.5)
            input("\nPress Enter to return to the menu...")

        elif choice == '2':
            while True:
                try:
                    money = float(input("Enter the amount to deposit: "))
                    if money <= 0:
                        print("Invalid amount")
                    else:
                        account.deposit(money)
                        break
                except ValueError:
                    print("The amount should be integer!")

            time.sleep(1.5)
            input("\nPress Enter to return to the menu...")

        elif choice == '3':
            while True:
                try:
                    money = float(input("Enter the amount to withdraw: "))
                    if money == 0:
                        print("Invalid amount! Cannot withdraw zero!")

                    if 0 < money <= account.balance:
                        account.withdraw(money)
                        break
                    else:
                        print("You don't have enough money!")
                        break
                except ValueError:
                    print("The amount should be integer!")

            time.sleep(1.5)
            input("\nPress Enter to return to the menu...")

        elif choice == '4':
            print("\nThank you for using this program q(≧▽≦q)")
            time.sleep(1)
            break
        else:
            print("Invalid choice! Try again.")
            time.sleep(1)
            input("\nPress Enter to return to the menu...")
