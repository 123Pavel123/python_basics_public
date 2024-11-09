from bank_account import BankAccount



def main():

    # alice_account = BankAccount("Alice")
    # bob_account = BankAccount("Bob", 520)

    bank_accounts = []
    with open("bank_accounts.txt", "r") as f:
        for line in f:
            name, account_number, balance = line.strip().split(",")
            bank_account = BankAccount(name, balance, account_number)
            bank_accounts.append(bank_account)

    [print(ba) for ba in bank_accounts]

    with open("bank_accounts_new.txt", "w") as f:
        for ba in bank_accounts:
            line = f"{ba.owner},{ba.account_number},{ba.balance}"
            f.write(line + "\n")


if __name__ == "__main__":
    main()
