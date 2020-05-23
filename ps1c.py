# -*- coding: utf-8 -*-
"""
Created on Sun May 10 12:52:35 2020

@author: danem
"""


portion_down_payment = 0.25
r = 0.04
annual_salary = float(input("enter your salary: "))
total_cost = 1000000
semi_annual_raise = 0.07
down_payment = portion_down_payment * total_cost
current_savings = 0

def calc_savings():
    current_savings = 0
    current_salary = annual_salary
    for i in range(36):
        current_savings += current_savings * r / 12 + current_salary / 12 * portion_saved     # Update savings monthly with interest and savings from salary
        if (i + 1) % 6 == 0:
            current_salary += current_salary * semi_annual_raise     # Add in raise every 6 months
    return current_savings

low = 0
high = 10000
portion_saved = 1
epsilon = 100
j = 0

if calc_savings() < down_payment - epsilon:
    print("It is not possible to pay the down payment in three years.")
else:
    while abs(current_savings - down_payment) > epsilon:
        avg = int(high + low) // 2     # Find midpoint for bisection search
        portion_saved = avg / 10000     # Convert the integer to a float between 0 and 1, representing the percent saved as a decimal
        current_savings = calc_savings()
        if current_savings > down_payment + epsilon:
            high = avg
        elif current_savings < down_payment - epsilon:
            low = avg
        j += 1
    print("Best savings rate:", portion_saved)
    print("Steps in bisection search:",j)
    print(current_savings)