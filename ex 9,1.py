transactions = []

for i in range(5):
    amount = float(input("Enter transaction amount: "))
    transactions.append(amount)


largest = max(transactions)
average = sum(transactions) / len(transactions)


print("Largest transaction:", largest)
print("Average spend:", average)