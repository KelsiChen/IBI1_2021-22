#import all the libraries
#os: enable us to operate files and folders in python.
#pandas: enable us to work with dataframes.
#numpy: enable us to use some useful mathematical functions.
#matplotlib.pyplot: enable us to do plotting work.
import os 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#go to the folder where the file we need is located.
os.chdir("/Users/chenyanxi/Desktop")

#using the library "pandas" to import the "full_data.csv" file
covid_data=pd.read_csv("full_data.csv")

#listing out the first and third columns in the .csv file
covid_data.iloc[10:21,1:4:2]

#Showing all rows related to Afghanistan using boolean: method 1
location=np.array(covid_data.iloc[:,1])
my_rows=location=="Afghanistan"
covid_data.loc[my_rows,"total_cases"]

#Showing all rows related to Afghanistan using boolean: method 2
L2=covid_data.loc[:,"location"]
Location2=np.array(L2)
my_rows=[]
for i in Location2:
	if i=="Afghanistan":
		my_rows.append(True)
	else:
		my_rows.append(False)
print(covid_data.loc[my_rows,"total_cases"])

#Showing all rows related to China using boolean: method 1
location=np.array(covid_data.iloc[:,1])
my_rows=location=="China"
covid_data.loc[my_rows,"total_cases"]


#Showing all rows related to China using boolean: method 2
L3=covid_data.loc[:,"location"]
Location3=np.array(L3)
my_rows=[]
for i in Location3:
        if i=="China":
                my_rows.append(True)
        else:
                my_rows.append(False)
print(covid_data.loc[my_rows,"total_cases"])


#calculate means of the new cases and new deaths in China
location=np.array(covid_data.iloc[:,1])
my_rows=location=="China"
a=np.array(covid_data.loc[my_rows,"new_cases"])
print("the average of the new cases in China=",np.mean(a))
b=np.array(covid_data.loc[my_rows,"new_deaths"])
print("the average of the new deaths in China=",np.mean(b))


#Creating a boxplot to show the data of new cases in China
China_new_cases=covid_data.loc[my_rows,"new_cases"]
China_new_deaths=covid_data.loc[my_rows,"new_deaths"]
plt.boxplot(x=[China_new_cases,China_new_deaths],
            vert = False,
            whis = 10,
            patch_artist = True,
            meanline = True,
            showbox = True,
            showcaps = True,
            showfliers = True,
            notch = False,
            labels=["new cases","new deaths"]
                )	
plt.title("China's new cases and new deaths")
plt.show()


#Plotting both new cases and new deaths in China over time
#b+/r+: blue/red "plus" sign(+)
china_dates=covid_data.loc[my_rows,"date"]
plt.plot(china_dates,China_new_cases,'b+')
plt.plot(china_dates,China_new_deaths,'r+')
plt.ylim(0,4500)
plt.xlabel("date")
plt.ylabel("case number")
plt.xticks(china_dates.iloc[0:len(china_dates):4],rotation=-90)
plt.title("China's new cases and new deaths: over time changing")
plt.show()

#the answer code of the question in the Question.txt
#question：How have new cases and total cases developed over time in Spain？
location=np.array(covid_data.iloc[:,1])
my_rows=location=="Spain"

Spain_new_cases=covid_data.loc[my_rows,"new_cases"]
Spain_total_cases=covid_data.loc[my_rows,"total_cases"] 
Spain_dates=covid_data.loc[my_rows,"date"]
plt.plot(Spain_dates,Spain_new_cases,'b-')
plt.plot(Spain_dates,Spain_total_cases,'ro')
plt.ylim(0,10000)
plt.xlabel("date")
plt.ylabel("case number")
plt.xticks(Spain_dates.iloc[0:len(Spain_dates):4],rotation=-90)
plt.title("Spain's new cases and total cases: over time changing")
plt.show()
