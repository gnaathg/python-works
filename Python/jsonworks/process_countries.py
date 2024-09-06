from json import load

f = open("D:\\luminarjune\\jsonworks\\countries.json",encoding="UTF-8")

data = load(f)

# print(len(data))

def return_country_by_name(name) :

    return [c for c in data if c.get("name") == name][0]


# print(return_country_by_name("India"))

# print(return_country_by_name("Afghanistan"))

country_data = return_country_by_name("Barbados")

if "regionalBlocs" in country_data :

    block_data = country_data.get("regionalBlocs")[0]

    # if "otherNames" in block_data :

        # print(block_data.get("otherNames"))

    # else :

        # print(country_data.get("name"))



def get_area(dic) :

    if "area" in dic :

        return dic.get("area")
    
    else :

        return 0
    

biggest_area_country = max(data,key=get_area)

# print(biggest_area_country.get("name"))


# for c in data :

#     for l in c.get("languages") :

#         if l.get("name") == "English" :

#             print(c.get("name"))


region_summary = {}

for c in data :

    region_name = c.get("region")

    area = 0

    if "area" in c :

        area = c.get("area")

    if region_name in region_summary :

        region_summary[region_name] += area

    else :

        region_summary[region_name] = area

# print(region_summary) 

key_values = [(k,v) for k,v in region_summary.items()]

print(key_values)