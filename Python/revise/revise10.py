# Write a program to count words in string 

def count_words(s):
    
    words = s.split()
    
    
    return len(words)


text = "Hello world! This is a Python program to count words."

word_count = count_words(text)

print(f"Number of words: {word_count}")
