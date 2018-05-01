

def calcBal(balance,annualInterestRate,monthlyPaymentRate):
    """
    balance: outstanding balance on card/float
    annualInterestRate: annual interest rate as decimal/float
    minMonthlyPayment: minimum monthly payment as decimal/float

    returns:
    balance at the end of 12 months after only paying the minimum, to two decimal places
    """
    
    month = 1 # set up counter to track months
    monthly_interest_rate = annualInterestRate / 12.0 # breakdown air into monthly rate

    while month <= 12:
        monthly_payment = balance * monthlyPaymentRate # calc monthly payment
        monthly_unpaid_balance = balance - monthly_payment # calc monthly unpaid balance
        updated_balance = monthly_unpaid_balance + (monthly_unpaid_balance * monthly_interest_rate) # calc updated balance
        balance = updated_balance # set prev balance to updated balance for next iteration
        month += 1 # increment month

    print('Remaining balance: ', round(updated_balance,2))

"""
# Test Case 1:
	      balance = 42
	      annualInterestRate = 0.2
	      monthlyPaymentRate = 0.04
	      
	      # Result Your Code Should Generate Below:
	      Remaining balance: 31.38
"""

calcBal(42,0.2,0.04)

