num = int(input("Enter a number:"))

is_prime = True

for i in range(2,num):

    if num % i == 0 :

        is_prime = False

        break
    
print(f"{num} is {'prime' if is_prime else 'not prime'}")    


