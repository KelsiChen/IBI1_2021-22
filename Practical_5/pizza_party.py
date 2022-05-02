#set the number of the cutting pieces goal
number=64

#the first situation is that just cut one time
n=1

#the number of pieces that i just cut one time
p=2

#while the number of pieces is smaller than the goal, calculate the number of pieces and cuts and print it out. Then cut one more time and repeat the above process.
while p<number:
	p=(n**2+n+2)/2
	print("the number of cuts is:",n,"the number of pizza is:",p)
	n+=1

