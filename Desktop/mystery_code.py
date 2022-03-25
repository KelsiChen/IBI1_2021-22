# What does this piece of code do?
# Ans: export a random integer between 1 and 100 for at most 10 times.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint
#random.randint(a, b) is used to generate an integer in a specified range
# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

#Progress equals 0 satisfies its condition of less than 10, and the while statement can be executed
progress=0

# Run it once and progress will be incremented by one
while progress<10:
	progress+=1
	n = randint(1,100)

#export a random integer between 1 and 100.
print(n)
