from json import load

f = open("D:\\luminarjune\\jsonworks\\films.json")

films = load(f)

for film in films :

    print(film.get("title"))