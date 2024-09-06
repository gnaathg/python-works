def is_fibonacci_number (num) :

    if num < 0 :

        return False
    
    if num == 0 :

        return True
    
    previous = 0 

    current = 1

    while (current <= num) :

        if current == num :

            return True
        
        next = previous + current

        previous = current 

        current = next

print(is_fibonacci_number(3))

