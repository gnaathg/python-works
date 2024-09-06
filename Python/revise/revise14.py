# Python program to print the elements of an array present on odd position 

def print_odd_position_elements(arr) :

    for index in range(len(arr)) :

        if index % 2 != 0 :

            print(f"Element at position {index} (odd position): {arr[index]}")

array = [10, 20, 30, 40, 50, 60, 70, 80]

print_odd_position_elements(array)