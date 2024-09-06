#  Python Program to Find Armstrong Number in an Interval 


def is_armstrong(num):

    num_str = str(num)

    power = len(num_str)

    return num == sum(int(digit) ** power for digit in num_str)

def find_armstrong_numbers(start, end):

    return [num for num in range(start, end + 1) if is_armstrong(num)]


start = int(input("Enter the starting number :"))

end = int(input("Enter the ending number:"))

print(f"Armstrong numbers between {start} and {end}: {find_armstrong_numbers(start, end)}")
