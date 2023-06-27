class Bank:
    def _init_(self):
        self.accounts = []
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_enabled = True

    def create_account(self, name, initial_balance):
        account = Account(name, initial_balance)
        self.accounts.append(account)
        self.total_balance += initial_balance

    def check_total_balance(self):
        return self.total_balance

    def check_total_loan_amount(self):
        return self.total_loan_amount

    def toggle_loan_feature(self, enabled):
        self.loan_enabled = enabled

    def get_account(self, name):
        for account in self.accounts:
            if account.name == name:
                return account
        return None


class Account:
    def _init_(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposit: +{amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: -{amount}")
        else:
            print("Insufficient balance!")

    def transfer(self, amount, recipient):
        if self.balance >= amount:
            self.balance -= amount
            recipient.deposit(amount)
            self.transaction_history.append(f"Transfer: -{amount} to {recipient.name}")
        else:
            print("Insufficient balance!")

    def take_loan(self):
        if bank.loan_enabled:
            loan_amount = 2 * self.balance
            self.balance += loan_amount
            bank.total_loan_amount += loan_amount
            self.transaction_history.append(f"Loan taken: +{loan_amount}")
        else:
            print("Loan feature is currently disabled.")


def print_transaction_history(account):
    print(f"Transaction history for {account.name}:")
    for transaction in account.transaction_history:
        print(transaction)



bank = Bank()

admin = Account("Admin", 0)


while True:
    print("\n--- Banking Management System ---")
    print("1. Admin Login")
    print("2. User Menu")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        # Admin login
        print("\n--- Admin Login ---")
        password = input("Enter admin password: ")

        if password == "admin123":
            print("\n--- Admin Menu ---")
            print("1. Create Account")
            print("2. Check Total Balance")
            print("3. Check Total Loan Amount")
            print("4. Toggle Loan Feature")
            print("5. Exit")

            admin_choice = int(input("Enter your choice: "))

            if admin_choice == 1:
                name = input("Enter account holder name: ")
                initial_balance = float(input("Enter initial balance: "))
                bank.create_account(name, initial_balance)
                print("Account created successfully!")

            elif admin_choice == 2:
                total_balance = bank.check_total_balance()
                print(f"Total balance: {total_balance}")

            elif admin_choice == 3:
                total_loan_amount = bank.check_total_loan_amount()
                print(f"Total loan amount: {total_loan_amount}")

            elif admin_choice == 4:
                enabled = input("Enter 'on' to enable loan feature or 'off' to disable it: ")
                if enabled == "on":
                    bank.toggle_loan_feature(True)
                    print("Loan feature enabled.")
                elif enabled == "off":
                    bank.toggle_loan_feature(False)
                    print("Loan feature disabled.")
                else:
                    print("Invalid choice.")

            elif admin_choice == 5:
                break

            else:
                print("Invalid choice.")

        else:
            print("Invalid password.")

    elif choice == 2:
        
        print("\n--- User Menu ---")
        name = input("Enter your name: ")
        account = bank.get_account(name)

        if account:
            print("\n1. Deposit Amount")
            print("2. Withdraw Amount")
            print("3. Check Available Balance")
            print("4. Transfer Amount")
            print("5. Check Transaction History")
            print("6. Take Loan")
            print("7. Exit")

            user_choice = int(input("Enter your choice: "))

            if user_choice == 1:
                amount = float(input("Enter the amount to deposit: "))
                account.deposit(amount)
                print("Amount deposited successfully!")

            elif user_choice == 2:
                amount = float(input("Enter the amount to withdraw: "))
                account.withdraw(amount)

            elif user_choice == 3:
                available_balance = account.balance
                print(f"Available balance: {available_balance}")

            elif user_choice == 4:
                recipient_name = input("Enter recipient's name: ")
                recipient_account = bank.get_account(recipient_name)
                if recipient_account:
                    amount = float(input("Enter the amount to transfer: "))
                    account.transfer(amount, recipient_account)
                    print("Amount transferred successfully!")
                else:
                    print("Recipient account not found.")

            elif user_choice == 5:
                print_transaction_history(account)

            elif user_choice == 6:
                account.take_loan()
                print("Loan taken successfully!")

            elif user_choice == 7:
                break

            else:
                print("Invalid choice.")

        else:
            print("User account not found.")

    elif choice == 3:
        break

    else:
        print("Invalid choice.")

print("Thank you for using the Banking Management System!")