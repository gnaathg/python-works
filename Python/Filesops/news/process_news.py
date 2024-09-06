f = open("D:\\luminarjune\\Filesops\\news\\news.txt","r")

# word_list = []

# for line in f :

#     words = line.rstrip("\n").split(" ")


#     for w in words :

#         word_list.append(w)

word_list = [w for line in f for w in line.rstrip("\n").split(" ")]

# print(word_list)

word_count = {word:word_list.count(word) for word in word_list}

# for word in word_list:

#     if word in word_count:

#         word_count[word] += 1

#     else:

#         word_count[word] = 1


# print(word_count)


def get_value(key) :

    return word_count.get(key)


srt = sorted(word_count,key =  get_value,reverse = True)

print(srt)
