text = "ABACBBDD"

word_count = {}

for ch in text :

    if ch in word_count :

       print(ch,"first recursive character") 

       break

    else :

        word_count[ch] = 1