from re import finditer

text = "ababbaabbaba"

matcher = finditer("ba",text) #

count = 0

for m in matcher :

    print(m.start(),"==",m.group())

    count += 1

print(count)
