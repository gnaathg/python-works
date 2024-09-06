number = [1,2,[3,(100,200,300),4],5,6]

num = number[2][1]

new_num = list(num)

print(new_num)

new_num.append(500)

print(new_num)

number[2][1] = tuple(new_num)

print(number) #[1, 2, [3, (100, 200, 300, 500), 4], 5, 6]