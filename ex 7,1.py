text = input("Enter the email text :" )

at_count = 0
dot_count = 0 
exelimation_count = 0

for ch in text:
    if ch == "@":
        at_count += 1
    elif ch == ".":
        dot_count += 1
    elif ch == "!":
        exelimation_count += 1

print("\n------EMAIL SCANING RESULT-------")

print("@ symbols",at_count)
print(". sumbols",dot_count)
print("! symbols",exelimation_count )