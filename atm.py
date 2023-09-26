class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        try:
            amount = float(amount)
            if amount > 0:
                self.balance += amount
                return f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}"
            else:
                return "Invalid deposit amount. Please enter a positive number."
        except ValueError:
            return "Invalid input. Please enter a valid number."

    def withdraw(self, amount):
        try:
            amount = float(amount)
            if 0 < amount <= self.balance:
                self.balance -= amount
                return f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"
            elif amount <= 0:
                return "Invalid withdrawal amount. Please enter a positive number."
            else:
                return "Insufficient funds. Please enter a smaller amount."
        except ValueError:
            return "Invalid input. Please enter a valid number."


def main():
    atm = ATM()  # Create an instance of the ATM class with an initial balance of 0

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Please select an option (1/2/3/4): ")

        if choice == '1':
            balance = atm.check_balance()
            print(f"Current Balance: ${balance:.2f}")

        elif choice == '2':
            amount = input("Enter the amount to deposit: $")
            result = atm.deposit(amount)
            print(result)

        elif choice == '3':
            amount = input("Enter the amount to withdraw: $")
            result = atm.withdraw(amount)
            print(result)

        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
