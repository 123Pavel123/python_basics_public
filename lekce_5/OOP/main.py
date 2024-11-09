from bank_account_original import BankAccount

def transfer(acc1, acc2, amount):
    acc1.withdraw(amount)
    acc2.deposit(amount)

def main():
    # Create accounts
    acc1 = BankAccount("Alice", 100)
    acc2 = BankAccount("Bob", 200)

    # Display accounts
    print(acc1)             # Uses __str__
    print(repr(acc2))       # Uses __repr__

    # Perform operations
    acc1.deposit(50)
    acc2.withdraw(30)

    # Compare accounts
    print(acc1 == acc2)     # False
    print(acc1 < acc2)      # True

    # Add accounts
    acc3 = acc1 + acc2
    print(acc3)

    # Test property
    acc1.balance = 300
    print(acc1.balance)

    # UKAZKA NACITANI ZE SOUBORU
    accounts = []
    with open("bank_accounts.txt", "r") as f:
        for line in f:
            owner, acc_number, balance = line.strip().split(",")
            accounts.append(BankAccount(owner, balance=float(balance), account_number=str(acc_number)))

    [print(acc) for acc in accounts]


if __name__ == "__main__":
    print("les't goooo")
    main()
