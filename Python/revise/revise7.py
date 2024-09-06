def is_harshad_number(number):
    # Convert the number to a string to iterate over digits
    num_str = str(number)
    
    # Calculate the sum of its digits
    sum_of_digits = sum(int(digit) for digit in num_str)
    
    # Check if the number is divisible by the sum of its digits
    return number % sum_of_digits == 0

num = int(input("Enter a number :"))

if is_harshad_number(num):

    print(f"{num} is a Harshad number.")

else:
    
    print(f"{num} is not a Harshad number.")
