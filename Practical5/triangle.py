#sum = (1+n)*n/2
#n is a variable in the range from 1 to 10, so I choose for loop.
#let n run from 1 to 10, and stops at 11
#if n is in the range(1,11),keep running; if n is out of the range,done.
n= 1
for n in range(1,11):
       sum = (1+n)*n/2
       n= n+1
       print(sum)
#in the range, 1 is included, 11 is not included
#the result is :
#1
#3
#6
#10
#15
#21
#28
#36
#45
#55
#the "#" in front of numbers can be omitted
