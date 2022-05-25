from xml.dom.minidom import parse
import xml.dom.minidom
import numpy as np
import matplotlib.pyplot as plt

DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")

number={}
data={}


for term in terms:
	parent_ids=[]
	ids=term.getElementsByTagName('id')[0]
	data[ids]=0

	for is_a in term.getElementsByTagName('is_a'):
		parent_ids.append(is_a.childNodes[0].data)
	number[ids]=parent_ids

for i in number.keys():
	parents=set()
	parent_ids=number[i]
	for parent_id in parent_ids:
		parents.add(parent_id)
	for parent in parents:
		data[parent] += 1

distribution=data.values()

plt.boxplot(distribution,
            vert = True,
            whis = 2.28,
            patch_artist = True,
            meanline = True,
            showbox = True,
            showcaps = False,
            showfliers = False,
            notch = False,
              )
plt.xlabel("total terms")
plt.ylabel("distribution of childnotes")
plt.title("the distribution of childnotes in all of the terms")

#show the boxplot.
plt.show()

term = []
node = []
translation = []

for i in term:
	x = i.getElementsByTagName("defstr")[0]
	y = i.getElementsByTagName("id")[0]
	defstr= x.childNodes[0]
	id = y.childNodes[0]
	if 'translation' in defstr.data:
		term.append(i)
	node.append(id)

for i in node:
	translation.append(data[i])


plt.boxplot(translation,
            vert = True,
            whis = 2.28,
            patch_artist = True,
            meanline = True,
            showbox = True,
            showcaps = False,
            showfliers = False,
            notch = False,
              )
plt.xlabel("total terms of 'translation'")
plt.ylabel("distribution of childnotes")
plt.title("the distribution of childnotes in terms with 'translation'")

#show the boxplot.
plt.show()


average1= sum(data.values())/len(data.values())
average2= sum(translation)/len(translation)
print("The overall Gene Ontology terms have", average1, "child nodes on average.")
print("The 'translation' terms have", average2, "child nodes on average.")

if average1 > average2:
   print("The 'translation' terms contains, on average, a greater number of child nodes than the overall Gene Ontology.")
else:
   print("The 'translation' terms contains, on average, a smaller number of child nodes than the overall Gene Ontology.")
        
            