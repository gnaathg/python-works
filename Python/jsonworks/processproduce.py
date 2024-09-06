from json import load

f = open("D:\\luminarjune\\jsonworks\\produce.json",encoding = "UTF-8")

items = load(f)

# print(len(items))

# for pr in items :

#     print(pr.get("title"))

item_title = [i.get("title") for i in items]

# print(item_title)

def get_count(c) :

        return c.get("rating").get("count")

user_count = max(items,key=get_count)

# most_user_rated = [i.get("title") for i in items if i.get("count") == user_count.get("count")]

print(user_count)

jewlery_items = [i.get("title") for i in items if i.get("category") == "jewelery"]

# print(jewlery_items)

above_100_rs = [i.get("title") for i in items if i.get("price") > 100]

# print(above_100_rs)

# random_range = [i.get("title") for i in items if i.get("price") in range (100,151)]

random_range = [i.get("title") for i in items if i.get("price") >= 100 and i.get("price") <= 150]

# print(random_range)