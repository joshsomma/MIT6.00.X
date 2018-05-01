"""
Test Case 1:
	      balance = 3329
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 310
"""
# test vars
balance = 3926
annualInterestRate = 0.2

# starting vars
lowest_payment = 0.01 # payment rate value to test and increment
monthly_interest_rate = annualInterestRate / 12.0 # APR split into monthly rate
prev_balance = balance
closing_balance = 0

while True:
	month = 1
	while month <= 12:
		monthly_unpaid_balance = prev_balance - lowest_payment
		updated_balance = monthly_unpaid_balance + (monthly_unpaid_balance * monthly_interest_rate)
		prev_balance = updated_balance
		month += 1
	closing_balance = round(updated_balance,2)
	if closing_balance <= 0:
		break
	prev_balance = balance
	lowest_payment += 0.01
print('Lowest payment: ', lowest_payment)