from json import load

f = open("D:\\luminarjune\\jsonworks\\mobiles.json")

products = load(f)

for p in products :

    print(p.get("title"))
