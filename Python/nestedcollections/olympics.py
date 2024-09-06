olympic_medal_count = [
    {"country": "United States", "gold": 39, "silver": 41, "bronze": 33},
    {"country": "China", "gold": 38, "silver": 32, "bronze": 18},
    {"country": "Japan", "gold": 27, "silver": 14, "bronze": 17},
    {"country": "Great Britain", "gold": 22, "silver": 21, "bronze": 22},
    {"country": "Russia", "gold": 20, "silver": 28, "bronze": 23},
    {"country": "Australia", "gold": 17, "silver": 7, "bronze": 22},
    {"country": "Netherlands", "gold": 10, "silver": 12, "bronze": 14},
    {"country": "France", "gold": 10, "silver": 12, "bronze": 11},
    {"country": "Germany", "gold": 10, "silver": 11, "bronze": 16},
    {"country": "Italy", "gold": 10, "silver": 10, "bronze": 20}
]

# country with most number of gold medals

def get_gold_medal(c):

    return c.get("gold")

most_gold_country = max(olympic_medal_count,key = get_gold_medal)

most_gold_earned_country = [c.get("country") for c in olympic_medal_count if c.get("gold") == most_gold_country.get("gold")  ]

print(most_gold_earned_country)

#medal count of each countries 


# country with least number of medals



# sort countries with medal count


# extra 5 questions