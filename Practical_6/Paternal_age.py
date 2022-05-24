#import these two Python package and name them with abbreviation, so that we can just type few letters instead of typing the whole terminology.
import numpy as np
import matplotlib.pyplot as plt

#store the paternal ages and the corresponding relative risk for congenitial heart disease in two separate lists.
paternal_age=[30,35,40,45,50,55,60,65,70,75]
chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]
x=paternal_age
y=chd

#combine the two lists into one dictionary with two axises.
paternal_ages_vs_chd=dict(zip(paternal_age,chd))
print(paternal_ages_vs_chd)

#show the scatter plot according to the above data.
plt.scatter(x,y,marker="o")
plt.xlabel("Paternal ages")
plt.ylabel("Relative risk of congenital heart disease")
plt.show

#use the package of random
import random

#input the paternal age and find the corresponding value in the index "chd", then print the correct risk of cardiovascular health in the offspring.
X=input("the paternal age is:")
Y=paternal_age.index(int(X))
print("the risk of cardiovascular health in the offspring is:", str(chd[Y]))
