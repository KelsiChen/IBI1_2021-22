from collections import Counter
from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt
import numpy as np

#Open the XML file.
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")


#Get the total number of terms.
length = terms.length
print("The total number of nodes is", length)


#Get the distribution of child nodes across terms.
number = []
for term in terms: 
    is_a = term.getElementsByTagName("is_a")
    node= len(is_a)
    number.append(node)


count = Counter(number)
print(count)
#The result is Counter({1: 23733, 2: 14172, 3: 4758, 0: 2294, 4: 1490, 5: 565, 6: 221, 7: 78, 8: 20, 9: 7, 10: 2})

#Draw the first chart.
nodenumber1=[0,1,2,3,4,5,6,7,8,9,10]
nodecount1=[2294,23733,14172,4758,1490,565,221,78,20,7,2]

x= nodenumber1
y= nodecount1

plt.bar(x,y,align='center',color='c',tick_label= [chr(i) for i in range(65, 75)])
plt.xlabel('The number of childnodes of each term')
plt.ylabel('The count of terms')
plt.title('The distribution of child nodes across all terms in the Gene Ontology')
plt.show()


#Get the number of terms associated with 'translation'.
term_list = []
for term in terms:
      defstr_text = term.getElementsByTagName("defstr")[0].childNodes[0]
      lines = defstr_text.data
      if 'translation' in lines:
          term_list.append(term)

number2 = []
for term in term_list: 
    is_a2 = term.getElementsByTagName("is_a")
    node2= len(is_a2)
    number2.append(node2)

count2 = Counter(number2)
print(count2)
#The result is "Counter({1: 128, 2: 117, 3: 37, 0: 9, 4: 3, 5: 1, 6: 1})"

#Draw the second distribution chart.
a=[0,1,2,3,4,5,6]
b=[9,128,117,37,3,1,1]

plt.bar(a,b,align='center',color='c',tick_label= [chr(i) for i in range(65, 75)])
plt.xlabel('The number of childnodes of terms associated with "translation"')
plt.ylabel('The count of terms')
plt.title('The distribution of child nodes across terms associated with "translation" ')
plt.show()

#Conclusion
#The overall Gene Ontology terms have 1.63 child nodes on average.
#The 'translation' terms have 1.68 child nodes on average.
#The 'translation' terms contain a greater number of child nodes than the overall Gene Ontology.

