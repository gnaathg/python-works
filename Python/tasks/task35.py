def is_armstrong_number(num) :

    num_str = str(num)

    num_digit = len(num_str)

    sum_of_powers = sum(int(digit)**num_digit for digit in num_str)

    return num == sum_of_powers

numbers = [151, 153, 154, 370, 371, 372, 373, 16341, 1635]

armstrong_numbers = [num for num in numbers if is_armstrong_number(num)]

print("Armstrong numbers:", armstrong_numbers)
