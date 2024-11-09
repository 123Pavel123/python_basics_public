import random


class BankAccount:
    info = "This is a bank account"

    def __init__(self, owner_name, balance=0, account_number=None):
        self.owner = owner_name
        self.__balance = balance
        if account_number is None:
            self.account_number = self.generate_account_number()
        else:
            self.account_number = account_number

    def __str__(self):
        return f"Bank account of {self.owner} with balance {self.__balance}, account number: {self.account_number}"

    def __repr__(self):
        return f"BankAccount('{self.owner}', {self.__balance})"

    def __eq__(self, other):
        return self.__balance == other.__balance

    def __lt__(self, other):
        return self.__balance < other.__balance

    def __gt__(self, other):
        return self.__balance > other.__balance

    @classmethod
    def generate_account_number(cls):
        account_number = ''.join(str(random.randint(0, 9)) for _ in range(9))
        bank_code = random.choice(["0300", "6002", "0965", "0800"])
        return f"{account_number}/{bank_code}"

    @property
    def balance(self):
        return int(self.__balance)

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        assert type(new_balance) == int or type(new_balance) == float, "Wrong type for setting balance"
        self.__balance = new_balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"${amount} deposited to {self.owner}'s account. New balance: ${self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Not enough money in the account.")
            return False

        self.__balance -= amount
        print(f"${amount} withdrawn from {self.owner}'s account. New balance: ${self.__balance}")

