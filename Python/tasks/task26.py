def is_palindrome(num) :

    original_num = num

    reverse_num = 0

    while (num != 0) :

        digit = num % 10

        reverse_num = reverse_num * 10 + digit

        num = num // 10

    print(f"The reversed num is {reverse_num}")    

    if  original_num == reverse_num :

        return True

    else :

        return False

print(is_palindrome(121))        