from re import fullmatch

g_mail = input("Enter your gmail:")

pattern = "\\w[\\w\\._]*+@gmail.com"

matcher = fullmatch(pattern,g_mail)

print("invalid" if matcher == None else "valid")

# + means match one or more
# ? means optional
# * zero or more
