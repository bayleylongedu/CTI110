# Bayley Long

# Ask the user how many pokemans they caught on Day 1, Day 2 and Day 3
# Print some statistics:


import matplotlib.pyplot as plt

# Collect the data
data = [] # empty list
print("Enter Pokeman Data:")
print("Day 1: ", end="")
day1 = int(input())
print("Day 2: ", end="")
day2 = int(input())
print("Day 3: ", end="")
day3 = int(input())

# Store these values in a list
data = [day1, day2, day3]

# Graph the real data
fig, ax = plt.subplots()
ax.plot([1, 2, 3], data)
plt.title ("Pokeman Data")
plt.xlabel('Number of Days')
plt.ylabel('Pokemans Collected')
plt.show()
