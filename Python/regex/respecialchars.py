from re import finditer

text = "abc KLe7fg@#"

# pattern = "\\d" #[0-9]

# pattern = "\\D" #[^0-9]

# pattern = "\\w" #[a-z A-Z 0-9]

# pattern = "\\W" #[^a-z A-Z 0-9]

# pattern ="\\s" #[space]

pattern ="\\S" #[^space]

matcher = finditer(pattern,text)

for m in matcher :

    print(m.start(),"==",m.group())