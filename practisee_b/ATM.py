class User:
    def __init__(self, acc, deposit):
        self.acc = acc
        self.deposit = deposit

class ATM(User):
    def __init__(self, acc, deposit, pin):
        super().__init__(acc, deposit)
        self.pin = pin

class Bank(ATM):
    def __init__(self, acc, deposit, pin):
        super().__init__(acc, deposit, pin)
        self.is_authenticated = False

    def pin_validation(self):
        attempts = 0
        while attempts < 4:
            enter_pin = int(input("Enter PIN: "))
            if enter_pin == self.pin:
                print("Successfully entered correct PIN.")
                self.is_authenticated = True
                return
            else:
                attempts += 1
                print("Incorrect PIN. Try again.")
        print("Sorry, limit exceeded. Card blocked.")
        exit()

    def withdraw(self, amount):
        if not self.is_authenticated:
            print("Please validate your PIN first.")
            return
        if amount > self.deposit:
            print("Insufficient funds.")
        else:
            self.deposit -= amount
            print(f"Withdrawal successful. Remaining Balance: ₹{self.deposit}")

    def balance(self):
        if not self.is_authenticated:
            print("Please validate your PIN first.")
        else:
            print(f"Current Balance: ₹{self.deposit}")

# Main Program
details = Bank(acc=125645, deposit=50000, pin=1234)

while True:
    print("\nATM Menu")
    print("1. PIN Validation")
    print("2. Check Balance")
    print("3. Cash Withdrawal")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        details.pin_validation()
    elif choice == 2:
        details.balance()
    elif choice == 3:
        if details.is_authenticated:
            amt = int(input("Enter amount to withdraw: ₹"))
            details.withdraw(amt)
        else:
            print("Please validate your PIN first.")
    elif choice == 4:
        print("Thank you for using the ATM.")
        break
    else:
        print("Invalid choice. Try again.")
