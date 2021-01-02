"""
Part B: Saving, with a raise
We are going to build on your solution to Part A by factoring in a raise every six months.
"""

r = 0.04
current_savings = 0
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
monthly_saved = portion_saved * (annual_salary / 12)

count = 0
while down_payment > current_savings:

    if count % 6 == 0 and count != 0:
        monthly_saved *= (1 + semi_annual_raise)

    current_savings = current_savings * (1 + r / 12) + monthly_saved
    count += 1

print(f'Number of months: {count}')

