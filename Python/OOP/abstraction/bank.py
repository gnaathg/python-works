class Bank:

    def __init__(self, ac_no: str, bank_name: str, balance: int, ac_type: str):
        self.ac_no = ac_no
        self.bank_name = bank_name
        self.balance = balance
        self.ac_type = ac_type

    def create_account(self, ac_no: str, balance: int, ac_type: str):
        self.ac_no = ac_no
        self.balance = balance
        self.ac_type = ac_type
        print(f"Account created: {self.ac_no}, Type: {self.ac_type}, Balance: {self.balance}")

    def deposit(self, amount: int):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount: int):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def display_details(self):
        print(f"Account Number: {self.ac_no}")
        print(f"Bank Name: {self.bank_name}")
        print(f"Account Type: {self.ac_type}")
        print(f"Balance: {self.balance}")

bank_instance = Bank("12345678","Federal Bank",12,"Premium")
bank_instance.create_account("12345",12,"Premium")
bank_instance.display_details()
bank_instance.deposit(2000)
bank_instance.withdraw(1000)