# write a program to find the sum of odd nums

#  write a program to find the count of odd and even nums

numbers = [1,3,5,6,4,2,8,9,10,12,33]

sum = 0

for i in numbers :

    if i % 2 != 0 :

        sum = sum + i

print(sum)
