

def is_Prime(num) :

    if num <= 1 :

        print("Not prime")

        return False
    
    for i in range (2,num) :

        if num % i == 0 :

            print("Not prime")

            return False

        else:

            print("Prime")

            return True

print(is_Prime(5)) 

print(is_Prime(7))

