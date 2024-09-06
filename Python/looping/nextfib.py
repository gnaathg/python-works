num = int(input("Enter a number:"))

previous = 0

current = 1

while (current <= num) :

    next = previous + current

    previous = current

    current = next

print(next)