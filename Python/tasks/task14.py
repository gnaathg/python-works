start_limit = int(input("Enter a starting number: "))

end_limit = int(input("Enter an ending number: "))

while start_limit <= end_limit:

    if start_limit % 2 != 0:

        print(start_limit)

    start_limit = start_limit + 1