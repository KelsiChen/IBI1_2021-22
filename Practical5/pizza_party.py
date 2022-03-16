#total number of slices
#    slice is p, and cuts is n
#    p=(n**2+n+2)/2

n=1
p=(n**2+n+2)/2

#calculate the total number of slices that can be cut from an increasing number of cuts
#print p when n plus 1
#if p<=64,keep running, if p>64, done.
#To meet the condition, while loop is chosen, for p do not to be defined as every number in the range and it will stop when the variable disobey the condition
#This programme starts when the number of cuts is 1
n=0
p=(n**2+n+2)/2
while p<=64:
        n+=1
        p=(n**2+n+2)/2
        print("The total number of slices of pizza is "+str(p)+" for "+str(n)+" cuts.")

#the results are:
#The total number of slices of pizza is 2 for 1 cuts.
#The total number of slices of pizza is 4 for 2 cuts.
#The total number of slices of pizza is 7 for 3 cuts.
#The total number of slices of pizza is 11 for 4 cuts.
#The total number of slices of pizza is 16 for 5 cuts.
#The total number of slices of pizza is 22 for 6 cuts.
#The total number of slices of pizza is 29 for 7 cuts.
#The total number of slices of pizza is 37 for 8 cuts.
#The total number of slices of pizza is 46 for 9 cuts.
#The total number of slices of pizza is 56 for 10 cuts.
#The total number of slices of pizza is 67 for 11 cuts.

#cut is increasing
#    if slice less than 64, keep running
#    if slice bigger than or equal to 64, done

n=1
p=(n**2+n+2)/2
while p<64:
        n+=1
        p=(n**2+n+2)/2
        if p > 64:
           break

print(n)

#The result is 11.
#n is the number of cuts when the slices is not less than 64 for the first time.
