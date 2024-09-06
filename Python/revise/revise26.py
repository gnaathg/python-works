# Write a Python program to print the numbers of a specified list after removing even numbers from it. 

def remove_even_numbers(lst):

    return [num for num in lst if num % 2 != 0]

lst = [1, 2, 3, 4, 5, 6]

print(f"Numbers after removing even numbers: {remove_even_numbers(lst)}")
