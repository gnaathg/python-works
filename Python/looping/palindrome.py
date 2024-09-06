num = int(input("Enter a number: "))

original_num = num

reverse_num = 0

while (num != 0):
    
    digit = num % 10

    reverse_num = reverse_num * 10 + digit

    num = num // 10

print(f"Reverse of the number is {reverse_num}")

if original_num == reverse_num:

    print("The number is palindrome")

else:

    print("The number is not palindrome")
    
