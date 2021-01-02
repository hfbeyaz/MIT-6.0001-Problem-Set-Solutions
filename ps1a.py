"""
Part A: House Hunting
We are going to determine how long it will take you to save
enough money to make the down payment in the problem set.
"""

r = 0.04
current_savings = 0
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
monthly_salary = annual_salary / 12
monthly_saved = portion_saved * monthly_salary
count = 0

while down_payment > current_savings:
    current_savings = current_savings * (1 + r / 12) + monthly_saved
    count += 1

print(f'Number of months: {count}')

