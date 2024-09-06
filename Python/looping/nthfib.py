num = int(input("Enter a number:"))

previous = 0

current = 1

if num < 0 :

    print("Invalid Input")

elif num == 0 :

    print(previous)

elif num == 1 :

    print(current)  

else : 

    for i in range (1,num + 1) :

        next = previous + current

        previous = current

        current = next

print(next)            