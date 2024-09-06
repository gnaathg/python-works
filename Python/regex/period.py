from re import findall

text = "the fat cat run very fast to catch the rat"

pattern = "\\b.at\\b"

matcher = findall(pattern,text)

print(matcher)