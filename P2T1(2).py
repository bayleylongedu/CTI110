# Bayley Long
# CTI-110
# 09/12/2023

import matplotlib.pyplot as plt

data = [] # empty list# New Version - loop and  get each day at a time
num_days = int(input("How many days? "))
for day in range(num_days):
  print("Day ", day, ":", end="")
  today = int(input())
  data.append(today) # add it to the end of the lsit
  
"""
print("Enter Pokeman Data:")
print("Day 1: ", end="")
day1 = int(input())
print("Day 2: ", end="")
day2 = int(input())
print("Day 3: ", end="")
day3 = int(input())
"""

# Graph the real data
fig, ax = plt.subplots()
ax.plot(range(num_days), data)
plt.title ("Pokeman Data")
plt.xlabel('Day Numeber')
plt.ylabel('Pokemans Collected')
plt.show()


