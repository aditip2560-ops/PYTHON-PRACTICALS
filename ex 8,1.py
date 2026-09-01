def senitizer_name(first_name,last_name):
    first_name= first_name.strip().title()
    last_name= last_name.strip().title()
    return f"{first_name }{last_name}"

first = input("Enter your first name: ")
last = input("Enter your last name: ")

full_name = senitizer_name(first,last)
print("clean name :",full_name)