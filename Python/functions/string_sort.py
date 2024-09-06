# text = "hello"

# sorted_text = sorted(text)

# print(sorted_text)

# sorted_text1 = sorted(text,reverse=True)

# print(sorted_text1)

# source_word = "listen"

# target_word = "silent"


def anagrams(source_word,target_word):

    if sorted(source_word) == sorted(target_word) :

        return "Anagram"
    
    else :

        return "Not Anagram"

print(anagrams('listen','silent'))

# srt_soure_wrd = sorted(source_word)

# srt_target_word = sorted(target_word)

# print(srt_soure_wrd==srt_target_word)