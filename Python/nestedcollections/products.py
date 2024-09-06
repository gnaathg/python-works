# List of dictionaries representing mobile phones with various attributes
mobiles = [
    {"id":100,"title":"s23 ultra","brand":"samsung","price":125000,"network":"5g"},
    {"id":101,"title":"s23","brand":"samsung","price":54000,"network":"4g"},
    {"id":102,"title":"edge14pro","brand":"moto","price":25000,"network":"5g"},
    {"id":103,"title":"edgeneo","brand":"moto","price":22000,"network":"4g"},
    {"id":104,"title":"redminote13pro","brand":"mi","price":25000,"network":"5g"},
    {"id":105,"title":"redmi13","brand":"mi","price":12000,"network":"4g"},
]

# Extracting the titles of all mobiles into a list
mobile_names = [nm.get("title") for nm in mobiles]


# Printing the list of mobile titles
print(f"Mobile names are :{mobile_names}.")

# Extracting the brands of all mobiles into a list
brands = [bnd.get("brand") for bnd in mobiles]

# Converting the list of brands to a set to get unique brand names
print(set(brands))

# Extracting the titles of all Samsung mobiles into a list
models = [mobile.get("title") for mobile in mobiles if mobile.get("brand") == "samsung"]

# Printing the list of Samsung mobile titles
print(f"Models of samsung are :{models}.")

# Extracting the titles of mobiles with prices in the range of 23000 to 40000
mobile_range = [mob.get("title") for mob in mobiles if mob.get("price") in range(23000, 40001)]

# Printing the list of mobile titles within the specified price range
print(f"Mobile titles within the specified price range of 23000 to 40000 are {mobile_range}.")

# Initializing the variable to keep track of the highest price found
max_price = 0

# Looping through each mobile in the list
for mob in mobiles:
    # Checking if the current mobile's price is higher than the max_price
    if mob.get("price") > max_price:
        # Updating max_price to the current mobile's price
        max_price = mob.get("price")

# Extracting the titles of mobiles with the highest price
luxury = [mob.get("title") for mob in mobiles if mob.get("price") == max_price]

# Printing the list of mobile titles with the highest price
print(f"Mobile titles with the highest price{luxury}")

# Function to get the price of a mobile
def get_price(mob):

    return mob.get("price")

# Finding the mobile with the highest price using the get_price function
costly_mob = max(mobiles, key=get_price)

# Finding the mobile with the lowest price using the get_price function
cheap_mob = min(mobiles, key=get_price)

# Printing the mobile with the lowest price
print(f"Mobile with the lowest price {cheap_mob}.")

# Printing the mobile with the highest price
print(f"Mobile with the highest price {costly_mob}.")

# Finding the mobile with the highest price using a lambda function
costly_ph = max(mobiles, key=lambda mob: mob.get("price"))

# Printing the mobile with the highest price using lambda
# print(costly_ph)

# Sorting the mobiles by price in ascending order using the get_price function
sorted_price = sorted(mobiles, key=get_price)

# Printing the list of mobiles sorted by price
print(f"Mobiles sorted by price : {sorted_price}.")

# Calculating the total price of all mobiles
total = sum([mob.get("price") for mob in mobiles])

# Printing the total price of all mobiles
print(f"Total price of all mobiles : {total}.")
