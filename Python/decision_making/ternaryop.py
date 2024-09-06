# num = 29

# # ternary operator

# print("Even" if num % 2 == 0 else  "Odd")

# print("Positive" if num > 0 else "Negative")

year = int(input("Enter a year: "))

result = "Leap year" if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) else "Not a leap year"

print(result)

