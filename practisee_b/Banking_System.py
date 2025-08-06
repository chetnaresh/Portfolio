class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Account(Customer):
    def __init__(self, name, age, account_type):
        super().__init__(name, age)
        self.account_type = account_type
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
        print(f"Account Type: {self.account_type}")
        print(f"Current Balance: ₹{self.balance}")

class SavingsAccount(Account):
    def __init__(self, name, age):
        super().__init__(name, age, "Savings")
        self.withdrawal_count = 0
        self.withdrawal_limit = 3  # Max 3 withdrawals

    def withdraw(self, amount):
        if self.withdrawal_count >= self.withdrawal_limit:
            print("Withdrawal limit exceeded for savings account.")
            return
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            self.withdrawal_count += 1
            print(f"Withdrew ₹{amount}. Remaining balance: ₹{self.balance}")

class CurrentAccount(Account):
    def __init__(self, name, age):
        super().__init__(name, age, "Current")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. Remaining balance: ₹{self.balance}")

class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        acc_type = input("Enter account type (savings/current): ").lower()
        if acc_type == 'savings':
            account = SavingsAccount(name, age)
        elif acc_type == 'current':
            account = CurrentAccount(name, age)
        else:
            print("Invalid account type!")
            return
        self.accounts.append(account)
        print("Account created successfully!")
        return account

    def operate(self, account):
        while True:
            print("\n1. Deposit\n2. Withdraw\n3. Display\n4. Exit")
            choice = input("Enter choice: ")
            if choice == '1':
                amt = int(input("Enter amount to deposit: "))
                account.deposit(amt)
            elif choice == '2':
                amt = int(input("Enter amount to withdraw: "))
                account.withdraw(amt)
            elif choice == '3':
                account.display()
            elif choice == '4':
                print("Exiting account...")
                break
            else:
                print("Invalid choice")

# Driver Code
bank = Bank()
user_account = bank.create_account()
if user_account:
    bank.operate(user_account)
