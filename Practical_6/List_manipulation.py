#import these two Python package and name them with abbreviation, so that we can just type few letters instead of a long terminology.#
import numpy as np
import matplotlib.pyplot as plt

#the total number of the marks are 8.
n=8

#store all the marks in a list, so that they could be easier to find and use.
marks=[45,36,86,57,53,92,65,45]

#the meaning of these terms:
#vert: whether it is vertical.
#whis: IQR(interquartile range).
#patch_artist: whether to fill the quartile box.
#meanline: whether there is a line showing the mean.
#showbox: whether it shows the box line.
#showcaps: whether it shows the maximum and minimum lines.
#showfliers: whether it shows the outliers.
#notch: whether there exists gaps in the middle of the box.
plt.boxplot(marks,
            vert = False,
            whis = 2.28,
            patch_artist = True,
            meanline = True,
            showbox = True,
            showcaps = False,
            showfliers = False,
            notch = False
              )

#show the boxplot.
plt.show()

#to compare the average mark Bob has received with the pass mark of 60%,we should first calculate the mean mark.
import numpy as np
average_mark=(45+36+86+57+53+92+65+45)/8
if average_mark>60:
	print("the average mark Rob has received across the eight practicals is higher than the pass mark of 60%")
else:
	print("the average mark Rob has received across the eight practicals is lower than the pass mark of 60%")
