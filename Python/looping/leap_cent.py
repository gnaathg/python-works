start_year = 1800

end_year = 2024

while start_year <= end_year:

    if (start_year % 100 != 0 and start_year % 4 == 0) or (start_year % 400) == 0 :

        print(start_year)

    start_year = start_year + 1
   