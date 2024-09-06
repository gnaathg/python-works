#  Python program to print the smallest element in an array 

def smallest_element(arr) :

    if not arr :

        return "Array is empty"
    

    return min(arr)


array = [10, 45, 32, 67, 89, 23]

smallest_element = smallest_element(array)

print(f"Smallest element of array is {smallest_element}")