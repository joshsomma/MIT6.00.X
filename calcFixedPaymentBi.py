"""
Test Case 1:
	      balance = 320000
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 29157.09
"""

# test vars
balance = 999999
annualInterestRate = 0.18

monthly_interest_rate = annualInterestRate / 12.0 # APR split into monthly rate
updated_balance = balance # var so we can keep original value of balance
closing_balance = 0 # var to test against
lower_bound = balance / 12
upper_bound = (balance * ((1 + monthly_interest_rate)**12)) / 12.0
lowest_payment = (upper_bound + lower_bound) / 2

while True:
    month = 1
    while month <= 12:
		monthly_unpaid_balance = updated_balance - lowest_payment
		updated_balance = monthly_unpaid_balance + (monthly_unpaid_balance * monthly_interest_rate)
		month += 1
    closing_balance = round(updated_balance,3)
    if closing_balance <= 0.05 and closing_balance >= 0.01:
        break
    elif closing_balance < 0.01:
        upper_bound = lowest_payment
        lowest_payment = (upper_bound + lower_bound) / 2
    else:
        lower_bound = lowest_payment
        lowest_payment = (upper_bound + lower_bound) / 2
    updated_balance = balance
print('Lowest payment: ', round(lowest_payment,2))



