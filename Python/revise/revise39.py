# Python program to print the multiplication table of a number
number = int(input("Enter the number: "))

print(f"Multiplication table for {number}:")

for i in range(1, 11):
    
    print(f"{number} x {i} = {number * i}")
