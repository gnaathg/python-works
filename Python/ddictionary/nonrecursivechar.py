text = "ABABCDE"

word_count = {}

for w in text :

    if w in word_count :

        word_count[w] += 1

    else :

        word_count[w] = 1

for w in text :

    if word_count[w] == 1 :

        print(w,"Non recursive")
