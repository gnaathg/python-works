word1 ="PQRST"

word2 = "ABC"

# output = PAQBRCST

word3 = ""

# len1, len2 = len(word1),len(word2)

# max_len = max(len1,len2)

# for i in range(max_len):

smallest_word = word1 if len(word1) < len(word2) else word2

for i in range (0,len(smallest_word)) :

    word3 = word3 + word1[i] + word2[i]

if len(word1) > len(word2) :

    balance = word1[len(smallest_word):]

else :

    balance = word2[len(smallest_word):]

word3 = word3 + balance

print(word3)    