#store data as key:value pairs, so that we can match the corresponding values together.
paternal_ages_vs_chd={'30':1.03,'35':1.07,'40':1.11,'45':1.17,'50':1.23,'55':1.32,'60':1.42,'65':1.55,'70':1.72,'75':1.94}

#show the information in the dictionary
print(paternal_ages_vs_chd)

#import these two Python package and name them with abbreviation, so that we can just type few letters instead of typing the whole terminology.
import numpy as np
import matplotlib.pyplot as plt

#store the paternal ages and the corresponding relative risk for congenitial heart disease in two separate lists.
paternal_age=[30,35,40,45,50,55,60,65,70,75]
chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]

#show the scatter plot according to the above data.
plt.scatter(paternal_age,chd,marker="o")

#use the package of random
import random

#randomly choose a pair of key and value from the paternal_ages_vs_chd dictionary.
a=random.sample(paternal_ages_vs_chd.items(),1)

#print the result
print(a)
