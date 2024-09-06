#  Program to Check Armstrong Numbers in Python 


def is_armstrong(num):

    num_str = str(num)

    power = len(num_str)

    return num == sum(int(digit) ** power for digit in num_str)


number = int(input("Enetr your number:"))

if is_armstrong(number):

    print(f"{number} is an Armstrong number.")

else:

    print(f"{number} is not an Armstrong number.")
