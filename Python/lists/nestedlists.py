number = [1,2,[3,[100,200,300],4],5,6]

print(number[2])

print(number[2][1])

number[2][1].append(500)

number[2][1].insert(1,600)

print(number)

print(len(number))