from re import fullmatch

passport_id = input("Enter your passport id:")

pattern = "[A-Z][1-9][0-9](0| )[0-9]{4}[1-9]"

# pattern = "[A-Z][1-9]\\d(0| )\\d{4}[1-9]"

matcher = fullmatch(pattern,passport_id)

print("invalid" if matcher == None else "valid")