
class BankAccount:
    def __init__(self):
        self.account_number = self.generate_account_number()
        print("WELCOME TO MIMI'S BANK, THE BANK OF LOVE")
        self.first_name = input("Kindly enter your first name: ")
        self.last_name = input("Kindly enter your last name: ")
        self.pin = input("Kindly enter  a 4-digit PIN that you won't forget: ")
        self.balance = 0

        def generate_account_number():
            account_number = [random.randint(6, 9)]
            for _ in range(9):
                account_number.append(random.randint(0, 9))
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Amount Deposited: ${amount}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"You Withdrew: ${amount}")
        else:
            print("Insufficient balance or invalid withdrawal amount.")

    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Balance: ${self.balance}")

def main():
    my_account = BankAccount()

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
        choice = input("Kindly Enter  your choice (1/2/3/4): ")

        if choice == '1':
            amount = float(input("Kindly enter amount to deposit: "))
            my_account.deposit(amount)
        elif choice == '2':
            amount = float(input("Kindly enter amount to withdraw: "))
            my_account.withdraw(amount)
        elif choice == '3':
            my_account.display_balance()
        elif choice == '4':
            print("Thank you for patronizing our bank app we will love to see your beautiful/handsome face again :)")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()

