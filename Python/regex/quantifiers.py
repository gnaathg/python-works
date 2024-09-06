from re import finditer

text = "acd345vvg@$%^c2v4t5"

# pattern = "[a-z]{3}" #prints 3 consecutive alphabets

pattern = "[a-z]{3}|[0-9]{3}" #a - z 3 consecutive times or 0 - 9 3 consecutive times

matcher = finditer(pattern,text)

for m in matcher :

    print(m.start(),"==",m.group())