from re import fullmatch

text = input("enter your text :")

pattern= "[k-m][0369][a-zA-Z0-9@]*"

matcher = fullmatch(pattern,text)

if matcher == None :

    print("invalid")

else :

    print("valid")