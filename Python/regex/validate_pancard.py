from re import fullmatch

pan_card = input("Enter pan card details :")

pattern ="[A-Z]{3}[PCAFHT][A-Z][0-9]{4}[A-Z]"

matcher = fullmatch(pattern,pan_card)

print("invalid" if matcher == None else "valid")