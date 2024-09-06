#  calculate bmi

weight = int(input("Enter your weight in kg:"))
height = int(input("Enter your height in cm:"))

bmi = weight/((height/100)**2)

print(f"Your bmi is {bmi}")