num = [22,3, 2, 5, 7, 1, 11, 10, 4]

largest_num = 0

second_largest = 0

for i in num :
        
    if i > largest_num:
            
            second_largest = largest_num

            largest_num = i

    elif i > second_largest and i != largest_num:
            
            second_largest = i

print(second_largest)
