"""
CTI110
P1HW1 - Variables
Bayley Long
9/5/23

Do some basic output with numbers
1. ask for an int
2. square it and then cube it
3. ask for another int
4. add them and multiply them

"""
# """
# PART ONE: VARIABLES
# variables, first and second
first = 0
second = 0

print("Enter integer:")
first = int(input()) # take input, then convert it to int
print(first, "squared is", first * first)
print("and", first, "cubed is", first * first * first, "!!")

# get another int
print("Enter another interget:")
second = int(input())
# TODO: print the number, not the words first and second
print(first, "+", second, "=", first + second)
print(first, "*", second, "=", first * second)
print()
# """

# PART TWO: MOVIES
# Three variables
# string - movie game
# int - the year of the movie
# float - the gross (in million dollars)
# string - a quote

name = "Interstellar"
year = 2014
gross = 701.7 # mil $

# Print out this information
print("The movie",name,"came out in",year,"and grossed",gross,"million worldwide.")

print()

# Then print out a quote from the movie
print("We've always defined ourselves by the ability to overcome the impossible. And we count these moments. These moments when we dare to aim higher, to break barriers, to reach for the stars, to make the unknown known. We count these moments as our proudest achievements. But we lost all that. Or perhaps we've just forgotten that we are still pioneers. And we've barely begun. And that our greatest accomplishments cannot be behind us, that our destiny lies above us.")

