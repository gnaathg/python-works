# Python Program to Find LCM

def find_lcm(x, y):
    
    lcm = max(x, y)
    
    
    while (lcm % x != 0) or (lcm % y != 0):
        lcm += 1
    
    return lcm


num1 = int(input("Enter your first number :"))

num2 = int(input("Enter your second number :"))

print(f"The LCM of {num1} and {num2} is {find_lcm(num1, num2)}")
