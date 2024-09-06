from re import fullmatch

text = input("Enter the vehicle registration :")

pattern = "(KL)(-)?[0-9]{2}(-)?[A-Z]{1,2}(-)?[0-9]{4}"

matcher = fullmatch(pattern,text)

print("invalid" if matcher == None else "valid")

