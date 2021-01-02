"""
The problem of finding a proper saving rate of income is solved by using bisection method
Considerations: - Using integers over decimals in bisection search
                - Using all re-assignments within the while loop
"""

annual_salary = float(input('Enter your annual salary: '))
current_savings = 0
total_cost = float(1000000)
semi_annual_raise = 0.07
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
r = 0.04                               # interest rate
epsilon = 100.0                        # desired proximity to the required down payment
num_steps = 0                          # steps taken to reach a value within the $100 of the required down payment
low = 0                                # low end of the range of values that our rate can take
high = max(0, 10000)                   # high end of the range of values that our rate can take
rate_uncorrected = (low + high) / 2    # the rate will be divided by 10000 to reflect a proper % later on.
                                       # the use of 10000 is to shun having infinite values between 0 and 1.
while abs(down_payment - current_savings) >= epsilon:

    num_steps += 1
    current_savings = 0
    rate = rate_uncorrected / 10000
    monthly_saved = rate * (annual_salary / 12)

    for month in range(36):

        if month % 6 == 0 and month != 0:
            monthly_saved *= (1 + semi_annual_raise)
        current_savings = current_savings * (1 + r / 12) + monthly_saved

    if down_payment > current_savings:
        low = rate_uncorrected
    else:
        high = rate_uncorrected
    rate_uncorrected = (low + high) / 2
#    print('low =', low/10000.0, 'high =', high/10000.0, 'rate =', rate) # run to see steps taken in the process
    if num_steps > 13:
        break

if num_steps > 13:
    print('It is not possible to pay the down payment in three years.')
else:
    print(f'Best savings rate: {rate:.4f}')
    print('Steps in bisection search: ', num_steps)

