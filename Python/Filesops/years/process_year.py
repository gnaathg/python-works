f_read = open("D:\\luminarjune\\Filesops\\years\\years.txt","r")

f_cent = open("D:\\luminarjune\\Filesops\\years\\century.txt","w")

f_non_cent = open("D:\\luminarjune\\Filesops\\years\\non_century.txt","w")

for year in f_read :

    y = int(year.rstrip("\n"))

    if y % 100 == 0 :

        f_cent.write(str(y) + "\n")

    else :

        f_non_cent.write(str(y) + "\n")