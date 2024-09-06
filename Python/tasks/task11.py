# bmi

height = int(input("Enter your height:"))

height_in_cm = height/100

weight = int(input("Enter your weight:"))

bmi = weight/height_in_cm**2

print(f"Bmi is :{bmi : 2f} ")

if bmi <= 19 :

    print ("Under weight!")

elif bmi <= 25 :

    print("Normal weight")    

elif bmi <= 30 :   

    print("Over weight!!") 

else:

    print("Obese!!!")    