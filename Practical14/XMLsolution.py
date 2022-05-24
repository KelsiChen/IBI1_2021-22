from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt
import numpy as np

#Open the XML file.
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")


#We need to find all child nodes of one node and its child nodes until it reaches the bottom.
#So we can get the number through calculating the number of parent nodes of the child nodes.
#This function can get the id  of parent nodes
def find_parents(node_id, parent_ids):
    mediate_ids = nodefamily[node_id]
    for mediate_id in mediate_ids:
        parent_ids.add(mediate_id) 
        find_parents(mediate_id, parent_ids)


nodefamily = {}
result_all = {}

#We need to get all nodes of each term
#The information will be stored in the nodefamily.
for term in terms:
    node_id = term.getElementsByTagName("id")[0].childNodes[0].data
    mediate_ids = []
    for is_a in term.getElementsByTagName("is_a"):
        mediate_ids.append(is_a.childNodes[0].data)
    nodefamily[node_id] = mediate_ids
    result_all[node_id] = 0

#Now we need to calculate all parent nodes of each child node.
#This equals the number of all child nodes of each parent node.
for key in nodefamily.keys():
    parent_ids = set()
    find_parents(key, parent_ids)
    for parent_id in parent_ids:
        result_all[parent_id] += 1

#Draw the plot of distribution of terms
plt.boxplot(result_all.values(), vert=True, whis=1.5, patch_artist=True, showbox=True, showcaps=True, showfliers=True)
plt.title('The distribution of child nodes across all terms in the Gene Ontology')
plt.xlabel("All terms in the Gene Ontology")
plt.ylabel("The number of childnodes of all terms in the Gene Ontology")
plt.show()



#Get the list of terms associated with 'translation'.
term_list = []
for term in terms:
      defstr_text = term.getElementsByTagName("defstr")[0].childNodes[0]
      if 'translation' in defstr_text.data:
          term_list.append(term)

#Find the nodes with translation in the nodefamily
node_list = []
for term in term_list:  
    node_id = term.getElementsByTagName("id")[0].childNodes[0].data 
    node_list.append(node_id)

result_translation = []
for node in node_list:
      result_translation.append(result_all[node])

#Draw the distribution plot
plt.boxplot(result_translation, vert=True, whis=1.5, patch_artist=True, showbox=True, showcaps=True, showfliers=True)
plt.title('The distribution of child nodes across terms associated with translation ')
plt.xlabel("Terms associated with translation")
plt.ylabel("number of childnodes of terms with translation")
plt.show()


#Calculate the average
average_all= sum(result_all.values())/len(result_all.values())
average_translation= sum(result_translation)/len(result_translation)
print("The overall Gene Ontology terms have", average_all, "child nodes on average.")
print("The 'translation' terms have", average_translation, "child nodes on average.")

if average_all > average_translation:
   print("The 'translation' terms contain a greater number of child nodes than the overall Gene Ontology terms.")
else:
   print("The overall Gene Ontology terms contain a greater number of child nodes than the 'translation' terms.")


#The overall Gene Ontology terms have 12.08177017321504 child nodes on average.
#The 'translation' terms have 13.486486486486486 child nodes on average.
#The overall Gene Ontology terms contain a greater number of child nodes than the 'translation' terms.
