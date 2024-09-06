# bmi

height = int(input("Enter your height:"))

height_in_cm = height/100

weight = int(input("enetr your weight:"))

bmi = weight/height_in_cm**2

print(f"Bmi is :{bmi}")