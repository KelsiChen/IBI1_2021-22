#The total number of triangle sequence is 10
number=10

#the initial sum is set as 0, which means that it could accumulate from the beginning.
sum=0

#we count the number of triangle sequence from the first one.
counter=1

#while the counter is smaller than number, it means that there still exists triangle sequences for us to count. Thus, after we count the sum of the balls number of this triangle sequence, we could move to the next one and count its balls sum.
while counter <= number:
	sum=sum+counter
	counter += 1

#print the sum of each triangle sequences.
print("sum:",sum)

