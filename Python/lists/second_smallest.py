number = [-20,2,5,7,1,9,10,4,-1]

# number.sort()

smallest_num =number[0]

second_smallest = number[-1]

for i in number :

    if i < smallest_num :

        second_smallest = smallest_num

        smallest_num = i

    elif i < second_smallest and i != smallest_num :    

        second_smallest = i

print(second_smallest)        