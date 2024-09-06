numbers = [1,3,5,6,4,2,8,9,10,12,33]

odd_count = 0

even_count = 0

for i in numbers :

    if i % 2 == 0 :

        even_count = even_count + 1

    if i % 2 != 0 :
            
        odd_count = odd_count + 1

print(odd_count)

print(even_count)

