
#import libraries，create the environment
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#os allows us to work with files and directories, and pandas is for working with dataframes.
os.chdir("C:\\Users\\50100\\Desktop")


#Importing the .csv file works
covid_data = pd.read_csv("full_data.csv")



#Showing the first and third columns from rows 10-20 (inclusive)
covid_data.iloc[10:21, [0,2]]

#Using a Boolean to show “total cases” for all rows corresponding to Afghanistan.
Location=covid_data.loc[ : ,"location"]
Location= np.array(Location)
my_rows=[]
for x in Location:
   if x=="Afghanistan":
    my_rows.append(True)
   else:
    my_rows.append(False)

print(covid_data.loc[my_rows, "total_cases" ])



#Using a Boolean to select all information about China.
Location=covid_data.loc[ : ,"location"]
Location= np.array(Location)
my_rows=[]
for x in Location:
   if x=="China":
    my_rows.append(True)
   else:
    my_rows.append(False)



#computed the mean number of new cases and new deaths in China.
china_new_cases=covid_data.loc[my_rows, "new_cases" ]
average_new_cases=sum(china_new_cases)/len(china_new_cases)
print(average_new_cases)
#Average of new cases in China is 893.9239130434783

china_new_deaths=covid_data.loc[my_rows, "new_deaths" ]
average_new_deaths=sum(china_new_deaths)/len(china_new_deaths)
print(average_new_deaths)
#Average of new deaths in China is 35.96739130434783



#The boxplot of new cases and new deaths in China
plt.boxplot([china_new_cases, china_new_deaths],
vert=True,
whis = 1.5,
patch_artist = True,
meanline = False,
showbox = True,
showcaps = True,
showfliers = False,
notch = False,
labels= [“New cases”, “New deaths”],
)
plt.ylabel("Case Numbers")
plt.title("Boxplot of new cases and new deaths in China")
plt.show()


#Plot describing both new cases and new deaths in China over time.
china_dates=covid_data.loc[my_rows, "date" ]
plt.plot(china_dates, china_new_cases, 'b-', label='New cases in China over time')
plt.plot(china_dates, china_new_deaths, 'r-', label='New deaths in China over time')
plt.title("New cases and new deaths in China over time")
plt.xlabel("Dates")
plt.ylabel("Numbers")
plt.xticks(china_dates.iloc[0:len(china_dates):4],rotation=-90)
plt.legend() #Use legends to label which color matches which subject
plt.show()

#"b+" is blue cross
#"r+" is red cross
#"bo" is blue circle
#"b-" is blue line


#Codes answering questions in question.txt

Location=covid_data.loc[ : ,"location"]
Location= np.array(Location)
my_rows=[]
for x in Location:
   if x=="United States":
    my_rows.append(True)
   else:
    my_rows.append(False)

US_total_cases=covid_data.loc[my_rows, "total_cases" ]
US_total_deaths=covid_data.loc[my_rows, "total_deaths" ]
US_dates=covid_data.loc[my_rows, "date" ]

plt.plot(US_dates, US_total_cases, 'b-', label='Total cases in the US over time')
plt.plot(US_dates, US_total_deaths, 'r-', label='Total deaths in the US over time')
plt.title("New cases and new deaths in the US over time")
plt.xlabel("Dates")
plt.ylabel("Numbers")
plt.xticks(US_dates.iloc[0:len(US_dates):4],rotation=-90)
plt.legend()
plt.show()
