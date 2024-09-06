#  fibonacci series

#  0 1 1 2 3 5 8 13 21 34 .....

num = int(input("Enter a number:"))

previous = 0

current = 1

print(f"{previous},{current}",end=",")

for i in range (1,num + 1) :

    next = previous + current

    previous = current

    current = next

    print(f"{next}",end=",")