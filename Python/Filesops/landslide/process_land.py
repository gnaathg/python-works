f = open("D:\\luminarjune\\Python\\Filesops\\landslide\\landslide.txt","r")

data = []

for line in f :

    lst = line.rstrip("\n").split(" ")

    dic = {"state" : lst[0],"year" : lst[1],"deaths" : int(lst[2])}

    data.append(dic)

print(data)    

def get_deaths (s) :

    return s.get("deaths")

most_death = max(data,key=get_deaths)

# year with max death

most_death_year = {y.get("year") for y in data if y.get("deaths") == most_death.get("deaths") }

# state withh max deaths

most_death_state = {y.get("state") for y in data if y.get("deaths") == most_death.get("deaths") }

print(f"Most death year is {most_death_year}.")

print(f"Most death state is {most_death_state}.")

# total number of deaths

def get_total_death(data) :

    return sum(item.get("deaths")for item in data)

total_deaths =get_total_death(data)

print(f"Total number of deaths is {total_deaths}.")

# average deaths

def get_average_death(data):

    total_deaths = get_total_death(data)

    count = len(data)

    return total_deaths / count if count > 0 else 0

average_death = get_average_death(data)

print(f"Average death is {average_death : .2f}.")

# death per state

state_summary = {}

for dic in data :

    state = dic.get("state")

    deaths = dic.get("deaths")

    if state in state_summary :

        state_summary[state] += deaths

    else :

        state_summary[state] = deaths

print(f"Deaths per state : {state_summary}")



