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
fig, ax = plt.subplots()
ax.boxplot(sortedmarks)
ax.set_xticklabels(["Rob"])
ax.set_ylabel("IBI Marks")
ax.set_xlabel("Student Name")

plt.show()

#calculate the average
sum(sortedmarks)
average=sum(sortedmarks)/len(sortedmarks)
#judge
if average>=60:
 print("Rob passed")
else:
 print("Rob failed")
#The result is "Rob failed"
#So Rob failed.
