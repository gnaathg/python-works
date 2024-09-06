#  Python program to print the largest element in an array

def find_largest_element(arr):
    
    if not arr:

        return "Array is empty"
    
    
    return max(arr)


array = [10, 45, 32, 67, 89, 23]

largest_element = find_largest_element(array)

print(f"The largest element is: {largest_element}")
