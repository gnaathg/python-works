def nth_digit_max (num1,num2) :

    # digit1 = num1 % 10

    # digit2 = num2 % 10

    # if digit1 > digit2 :

    #     print(f"{num1} is largest")

    # else :

    #     print(f"{num2} is largest")    

    return num1 if num1 % 10 > num2 % 10 else  num2

print(nth_digit_max(123,890))    