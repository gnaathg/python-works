marks = float(input("Enter your mark :"))

if marks > 90 or marks <= 100 :

    print("A grade")

elif marks > 80 or marks <= 90 :

    print("B grade")

elif marks >= 70 or marks <= 80 :

    print("C grade")

elif marks <= 70 :

    print("Fail")

else:

    print("invalid input")
