#create a dictionary when I have two arrays
#define the x-axis and y-axis
#draw a plotmap
#show the plotmap
#choose an age
#print the relative rate of the age

#create a dictionary when I have two arrays
paternal_age=[30,35,40,45,50,55,60,65,70,75]
chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]
dict1=dict(zip(paternal_age,chd)) #Use dict(zip()) to add the two arrays together
print(dict1)

#draw a plotmap
import numpy as np
import matplotlib.pyplot as plt

#define the x-axis and y-axis
x= paternal_age
y= chd

plt.scatter(x, y, marker='o')
plt.show()

#Here the paternal age I choose is 50. 
print(dict1[50])
#and the relative rate is 1.23,which is correct to the age 50.
