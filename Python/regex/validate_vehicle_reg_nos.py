from re import fullmatch

f = open("D:\\luminarjune\\regex\\vehicle_reg_nos.txt","r")

pattern = "(KL)\\s[0-9]{2}\\s[A-Z]{1,2}\\s[0-9]{4}"

out_file = open("D:\\luminarjune\\regex\\valid_reg_nos.txt", "a")

for line in f :

    register = line.rstrip("\n")

    matcher = fullmatch(pattern,register)

    if matcher != None :

        print(register)

        out_file.write(register + "\n")

