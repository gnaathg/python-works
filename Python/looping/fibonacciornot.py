num = int(input("Enter a number :"))

previous = 0 

current = 1

is_Fib = False

if num in (0,1) :

    is_Fib = True

else :   

    next = previous + current 

    while (next <= num) :

        next = previous + current

        if (next == num) :

            is_Fib = True

            break

        previous = current

        current = next

print(is_Fib)    
