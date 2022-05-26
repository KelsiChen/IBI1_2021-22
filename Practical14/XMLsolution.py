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
	ids=term.getElementsByTagName('id')[0].childNodes[0].data
	data[ids]=0
	for is_a in term.getElementsByTagName('is_a'):
		parent_ids.append(is_a.childNodes[0].data)
	number[ids]=parent_ids

#find all the parent nodes of each child nodes: this part of the codes was taught by one of my friends. He taught me the basic logic of the program, and I imitated his writing logic.
def nodes_number(id, parents):
	parent_ids=number[id]
	for parent_id in parent_ids:
		parents.add(parent_id)
		nodes_number(parent_id,parents)

for i in number.keys():
	parents=set()
	nodes_number(i,parents)
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
            showfliers = True,
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

for i in terms:
	x = i.getElementsByTagName("defstr")[0]
	defstr=x.childNodes[0]
	if 'translation' in defstr.data:
		term.append(i)

for i in term:

	y = i.getElementsByTagName("id")[0]
	id = y.childNodes[0]
	node.append(id.data)

for i in node:
	translation.append(data[i])


plt.boxplot(translation,
            vert = True,
            whis = 2.28,
            patch_artist = True,
            meanline = True,
            showbox = True,
            showcaps = False,
            showfliers = True,
            notch = False,
              )
plt.xlabel("total terms of 'translation'")
plt.ylabel("distribution of childnotes")
plt.title("the distribution of childnotes in terms with 'translation'")

#show the boxplot.
plt.show()


total_sum=sum(data.values())
total_translation=sum(translation)

average1= total_sum/len(data.values())
average2= total_translation/len(translation)
print("The overall Gene Ontology terms have", average1, "child nodes on average.")
print("The 'translation' terms have", average2, "child nodes on average.")

if average1 > average2:
   print("The 'translation' terms contains, on average, a greater number of child nodes than the overall Gene Ontology.")
else:
   print("The 'translation' terms contains, on average, a smaller number of child nodes than the overall Gene Ontology.")
