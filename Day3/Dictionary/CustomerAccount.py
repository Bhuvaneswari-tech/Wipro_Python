# Initialize customer accounts
accounts = {
    101: {"name": "Alice", "type": "Savings", "balance": 5000},
    102: {"name": "Bob", "type": "Current", "balance": 12000},
    103: {"name": "Charlie", "type": "Savings", "balance": 7000},
    104: {"name": "Diana", "type": "Current", "balance": 15000}
}

# 1. Deposit 2000 to Account 101
accounts[101]["balance"] += 2000

# 2. Withdraw 5000 from Account 102
accounts[102]["balance"] -= 5000

# 3. Add new account 105 (Eve)
accounts[105] = {"name": "Eve", "type": "Savings", "balance": 8000}

# 4. Close Account 103
accounts.pop(103)

# 5. List all customer accounts
print("Customer Accounts:")
for acc_no, details in accounts.items():
    print(f"Account {acc_no}: {details['name']} - {details['type']} - Balance: {details['balance']}")
