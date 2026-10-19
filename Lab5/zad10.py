def address_transactions(transactions, addr):
    selected = [
        tx for tx in transactions
        if tx["from"] == addr or tx["to"] == addr
    ]

    balance = 0

    for tx in selected:
        if tx["to"] == addr:
            balance += tx["amount"]

        if tx["from"] == addr:
            balance -= tx["amount"]

    return selected, balance

transactions = [
    {"from": "Alice", "to": "Bob", "amount": 50},
    {"from": "Bob", "to": "Alice", "amount": 20},
    {"from": "Alice", "to": "Carol", "amount": 10}
]

selected, balance = address_transactions(
    transactions, "Alice"
)

print(f"Транзакции Alice ({len(selected)}):")

for tx in selected:
    print(
        f"  {tx['from']} -> {tx['to']}: "
        f"{tx['amount']}"
    )

print(f"Баланс Alice: {balance}")