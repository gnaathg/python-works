from re import finditer

text = "abc123@#$*fvhBNMJUO"

# pattern = "[abf]" #check either a or b  or f

# pattern = "[a-k]" #check either from a to k

# pattern = "[A-Za-z]"

# pattern = "[a-zA-Z0-9@#$*]"

pattern = "[^0-9 a-z A-Z]" # except 0-9 a-z A-Z ^ means except


matcher = finditer(pattern,text)

for m in matcher :

    print(m.start(),"==",m.group())