# word = "hello"

# print(word.capitalize()) #Hello

# print(word.casefold()) #hello

# print(word.upper()) #HELLO

# print(word.lower()) #hello

# print(word.index("o")) #4

# print(word.isalnum()) #True

# print(word.isalpha()) #True

# print(word.isdigit()) #False

# email_id = "sabarinathg6 @gmail.com"

# user_name,mail = email_id.split(" ")

# print(user_name)

# print(mail)

# word = "/nhello world/n"

# print(word.startswith("he"))

# print(word.startswith("e"))

# print(word.startswith("He"))

# print(word.endswith("ld"))

# print(word.endswith("l"))

# print(word.endswith("lD"))

# print(word.strip("/n"))  

# print(word.rstrip("/n")) #remove from right side

# print(word.lstrip("/n")) #remove from left side

# print(word.replace("/n",""))

text = "hellopython"

sliced_word = text[:5]

print(sliced_word)

sliced_word = text[5:]

print(sliced_word)

sliced_word = text[0:5]

print(sliced_word)

sliced_word = text[10:4:-1]

print(sliced_word)

sliced_word = text[ : : -1]

print(sliced_word)

# email_id = "sabarinathg6@gmail.com"

# index_pos = email_id.index("@")

# user_name = email_id[:index_pos]

# print(user_name)

# domain_name = email_id[index_pos:]

# print(domain_name)