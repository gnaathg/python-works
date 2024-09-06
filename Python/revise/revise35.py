# Python program to find the maximum and minimum numbers in a list
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

max_num = max(numbers)

min_num = min(numbers)

print("The maximum number is:", max_num)

print("The minimum number is:", min_num)
