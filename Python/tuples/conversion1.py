numbers = [1,2,[3,(100,200,300),4],5,6]

num = numbers[2][1]

num_nw = list(num)

# print(num_nw) [100, 200, 300]

num_nw.insert(1,150)

numbers[2][1] = tuple(num_nw) 

# print(numbers) #[1, 2, [3, (100, 150, 200, 300), 4], 5, 6]

pop = numbers.pop(2)

pop.pop(2)

#print(pop) #not needed [3, (100, 150, 200, 300)]

pop.insert(1,4)

print(pop) # not needed [3, 4, (100, 150, 200, 300)]

numbers.insert(2,pop)

print(numbers) #[1, 2, [3, 4, (100, 150, 200, 300)], 5, 6]






# numbers = [1, 2, [3, (100, 200, 300), 4], 5, 6]

# Extract the tuple and convert it to a list

# num_nw = list(numbers[2][1])

# Insert the new value

# num_nw.insert(1, 150)

# Update the tuple in the original list

# numbers[2][1] = tuple(num_nw)

# Extract and modify the sublist

# sublist = numbers.pop(2)
# sublist.pop(2)  # Remove the element at index 2
# sublist.insert(1, 4)

# Insert the modified sublist back into the main list

# numbers.insert(2, sublist)

# print(numbers)  # [1, 2, [3, 4, (100, 150, 200, 300)], 5, 6]
