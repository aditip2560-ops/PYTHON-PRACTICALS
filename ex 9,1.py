# Consumer Transaction Tracking Program

transactions = []


for i in range(5):
    amount = float(input(f"Enter transaction {i + 1}: ₹"))
    transactions.append(amount)


largest = max(transactions)


average = sum(transactions) / len(transactions)


print("\n--- Transaction Summary ---")
print("Transaction values:", transactions)
print(f"Largest transaction: ₹{largest:.2f}")
print(f"Average spending: ₹{average:.2f}")