#  How to count the number of upper and lowercase letters in a string  

def count_upper_lower(s):
    
    upper_count = 0

    lower_count = 0
    
   
    for char in s:

        if char.isupper():

            upper_count += 1

        elif char.islower():

            lower_count += 1
    
    return upper_count, lower_count


text = "Hello World! This is a Python Program."

upper_count, lower_count = count_upper_lower(text)

print(f"Number of uppercase letters: {upper_count}")

print(f"Number of lowercase letters: {lower_count}")
