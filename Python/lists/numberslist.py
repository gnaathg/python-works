numbers = [10,11,12,34,48,55,67,98]

print(len(numbers))

for i in range(0,len(numbers)) :

    if numbers[i] % 2 == 0:

        print(numbers[i])

total = 0 

for i in range(0,len(numbers)) :

    total += numbers[i]

print(f"Total ={total}") 


odd_total = 0


for i in range(0,len(numbers)) :

    if numbers[i] % 2 != 0 :

        odd_total += numbers[i]

print(f"Odd total ={odd_total}")









