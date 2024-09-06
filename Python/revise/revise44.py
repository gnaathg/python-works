# Python program to calculate discount based on purchase quantity
quantity = int(input("Enter the quantity: "))

cost_per_unit = 100

total_cost = quantity * cost_per_unit

if total_cost > 1000:
    
    total_cost *= 0.9  

print(f"The total cost is: {total_cost}")
