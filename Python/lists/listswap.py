num = [1,2,2,3,4,5,3,6,7,4,8]

# num[-1],num[0] = num[0],num[-1]

# print(num)

# odd = []

# for i in num :

#     if i % 2 != 0 :

#         odd.append(i)

# print(odd)

# for i in num :
     
#     if i % 2 == 0 :

#         num.remove(i)

# print(num)        

num1 = []

for i in num :

    if num.count(i) == 1 :

        print(i)

        num1.append(i)

print(num1)