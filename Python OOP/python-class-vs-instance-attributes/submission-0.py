class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_balance = 0
    total_accounts = 0
    
    def __init__(self, name, account_balance) -> None:
        self.name = name
        self.balance = account_balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += account_balance


# TODO: Create two accounts
# TODO: Print the information using the mentioned format

alice_acc = BankAccount("Alice", 1000)
bob_acc = BankAccount("Bob", 2000)

print(f"Alice's balance: ${alice_acc.balance}")
print(f"Bob's balance: ${bob_acc.balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")