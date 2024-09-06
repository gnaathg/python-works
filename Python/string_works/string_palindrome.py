def is_palindrome(str) :

    # if str[::-1] == str :

    #     return True
    
    # else:

    #     return False

    reversed_str = str[::-1]

    return str == reversed_str
    
print(is_palindrome("sabbas"))    

print(is_palindrome("abcd"))