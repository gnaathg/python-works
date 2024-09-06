#  calculate monthly emi
#  loan amount
#  tenure
#  interest rate

laon_amount = int(input("Enter your amount:"))

loan_tenure = int(input("Enter your tenure :"))

interest_rate = float(input("Enter your interest rate:"))

monthly_interest = interest_rate/(12*100)

tenure_in_months = loan_tenure*12

# EMI = P * r * (1 + r)^n / ((1 + r)^n - 1)

emi = laon_amount*monthly_interest*(1+monthly_interest)**tenure_in_months/((1+monthly_interest)**tenure_in_months-1)

print(f"Your emi is {emi : .2f}")

total_amount_payable = emi*tenure_in_months

print(f"Total amount payable {total_amount_payable : .2f}")

total_interest_payable = total_amount_payable - laon_amount

print(f"Total interest payable {total_interest_payable : .2f}")

