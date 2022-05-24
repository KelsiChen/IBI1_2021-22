# What does this piece of code do?
# Answer: Make the loop run 10 times to choose ten random numbers between 1 and 100 and then print the last number.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
# lower limit is included in the randint(), but upper limit is not included.
# the number from randint will be integers
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
#the number may no be integers, so we need to use ceil to control it.
from math import ceil

progress=0
# a variable called progress is defined
while progress<10:
	progress+=1 #the progress will add 1 when doing one loop until progress=10
	n = randint(1,100) #every loop n will be a random number

print(n) #print n in the last loop

# the results will be a random number in 1 to 99
