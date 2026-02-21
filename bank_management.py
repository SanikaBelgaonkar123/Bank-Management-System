import os

class BankAccount:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self):
        try:
            acc_no = input("Enter Account Number: ")
            name = input("Enter Name: ")
            balance = float(input("Enter Initial Balance: "))

            if acc_no in self.accounts:
                print("Account already exists!")
            else:
                self.accounts[acc_no] = {"name": name, "balance": balance}
                self.save_to_file()
                print("Account Created Successfully!")
        except ValueError:
            print("Invalid input! Please enter correct data.")

    def deposit(self):
        try:
            acc_no = input("Enter Account Number: ")
            amount = float(input("Enter Deposit Amount: "))

            if acc_no in self.accounts:
                self.accounts[acc_no]["balance"] += amount
                self.save_to_file()
                print("Amount Deposited Successfully!")
            else:
                print("Account not found!")
        except ValueError:
            print("Invalid amount!")

    def withdraw(self):
        try:
            acc_no = input("Enter Account Number: ")
            amount = float(input("Enter Withdraw Amount: "))

            if acc_no in self.accounts:
                if self.accounts[acc_no]["balance"] >= amount:
                    self.accounts[acc_no]["balance"] -= amount
                    self.save_to_file()
                    print("Withdrawal Successful!")
                else:
                    print("Insufficient Balance!")
            else:
                print("Account not found!")
        except ValueError:
            print("Invalid amount!")

    def check_balance(self):
        acc_no = input("Enter Account Number: ")
        if acc_no in self.accounts:
            print("Account Holder:", self.accounts[acc_no]["name"])
            print("Balance:", self.accounts[acc_no]["balance"])
        else:
            print("Account not found!")

    def save_to_file(self):
        with open("bank_data.txt", "w") as file:
            for acc_no, data in self.accounts.items():
                file.write(f"{acc_no},{data['name']},{data['balance']}\n")

    def load_from_file(self):
        if os.path.exists("bank_data.txt"):
            with open("bank_data.txt", "r") as file:
                for line in file:
                    acc_no, name, balance = line.strip().split(",")
                    self.accounts[acc_no] = {
                        "name": name,
                        "balance": float(balance)
                    }


# Menu-driven CLI
def main():
    bank = BankAccount()

    while True:
        print("\n===== BANK MANAGEMENT SYSTEM =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            bank.create_account()
        elif choice == "2":
            bank.deposit()
        elif choice == "3":
            bank.withdraw()
        elif choice == "4":
            bank.check_balance()
        elif choice == "5":
            print("Thank You!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()