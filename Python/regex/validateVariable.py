from re import fullmatch

variable = input("Enter variable name :")

pattern = "[a-zA-Z][a-zA-Z0-9_]*"

matcher = fullmatch(pattern,variable)

print("invalid" if matcher == None else "valid")

