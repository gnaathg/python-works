year = int(input("Enter the year:"))

if (year % 400 == 0) and (year % 100 != 0 or year % 4 ==0) :

    print("leap year")

else:

    print("Non-leap year")