from re import fullmatch

phone = input("Enter the number :")

pattern = "(91)\\s?[6-9]\\d{9}"

matcher = fullmatch(pattern,phone)

print("invalid" if matcher == None else "valid")
