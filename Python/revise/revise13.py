#   Python program to print the elements of an array present on even position 

def print_even_position_elements(arr):
    
    for index in range(len(arr)):
        
        if index % 2 == 0:

            print(f"Element at position {index} (even position): {arr[index]}")


array = [10, 20, 30, 40, 50, 60, 70, 80]

print_even_position_elements(array)
