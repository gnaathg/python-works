words = ["madam","aba","bcb","hello","python"]

for word in words :

    rev_word = word[::-1]

    if rev_word == word :

        print(f"{word} is palindrome")

    else :

        print(f"{word} is not palindrome")

          