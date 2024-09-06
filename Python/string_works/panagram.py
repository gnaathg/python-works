text = "The quick brown fox jumps over a lazy dog"

text = text.casefold()

print(text)

for ch in "abcdefghijklmnopqrstuvwxyz" :

    # if ch not in text :

    #     print("not a panagram")

    #     break

    # else :

    #     print("panagram")

    #     break


    if text.count(ch) == 0 :

        print("Not a panagram")

    else :

        print("Panagram")

        break    
