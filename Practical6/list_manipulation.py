#create and sort the array, 
#then draw the boxplot of it,
#then calculate the average and judge.

#create the array
marks=[45,36,86,57,53,92,65,45]
#sort the array
sorted(marks)
sortedmarks= sorted(marks)
print(sortedmarks)

#draw the boxplot
import matplotlib.pyplot as plt
plt.boxplot(sortedmarks,
vert=True,
whis = 1.5,
patch_artist = True,
meanline = False,
showbox = True,
showcaps = True,
showfliers = True,
notch = False
)
plt.show()

#calculate the average
sum(sortedmarks)
average=sum(sortedmarks)/len(sortedmarks)
#judge
print(average>=60)

#The result is False, so the average is below 60, 
#So Rob failed.
