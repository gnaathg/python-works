#  Write a Python function to find the maximum of three numbers.

def max_of_three(num1, num2, num3):

    return max(num1, num2, num3)

num1 = int(input("Enter the first number:"))

num2 = int(input("Enter the second number :"))

num3 = int(input("Enter the third number :"))


print(f"Maximum of {num1}, {num2}, and {num3} is {max_of_three(num1, num2, num3)}")
