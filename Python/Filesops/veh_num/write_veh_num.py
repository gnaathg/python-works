vehicle_numbers = ["KL-29-N-6212"
                   "KL-04-j-6703"
                   "KL-29-c-3888"
]

f = open("D:\\luminarjune\\Filesops\\veh_num.txt","w")

for vehicle in vehicle_numbers :

    f.write(str(vehicle) + "\n")