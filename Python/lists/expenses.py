expenses = [10000,15000,16000,20000,30000,400000]

expenses_count = len(expenses)



for i in range (0,expenses_count) :

    print(expenses[i])

print(expenses_count) #6 - count




for i in range (0,expenses_count) :

    if expenses[i] > 15000 :

        print(expenses[i])




total_expense = 0

for i in range(0, len(expenses)) :

    total_expense = total_expense + expenses[i]

print(f"Total expenses = {total_expense}")  




for i in range (0,len(expenses)) :

    average_expenses = total_expense/len(expenses)

print(f"Average expenses = {average_expenses }")    









