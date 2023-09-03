# This program calculates and displays travel expenses.
# 09/02/2023
# CTI-110 P1HW2 - Travel Expense
# Bayley Long
#

# Ask the user to enter their budget
budget = int(input('What is your budget?'))

# Ask the user to enter travel destination
destination = input('Where are you travling to?')

# Ask the user how much they will spend on gas
gas = int(input('How much are you going to spend on gas?'))

# Ask the user how much they will spend on accommodations
accommodation = int(input('How much are you spending on accommodations?'))

# Ask the user how much they will spend on food
food = int(input('How much will you spend on food?'))

# Calculate the total expenses
total_expenses = gas + accommodation + food
# Calculate the remaining balance
remaining_balance = budget - total_expenses

# Display the results
print()
print('--------Travel Expenses--------')
print('Location:', destination)
print('Initial Budget:', budget)
print()
print('Gas:', gas)
print('Accommodation:', accommodation)
print('Food:', food)
print()
print('Remaining Balance', remaining_balance)