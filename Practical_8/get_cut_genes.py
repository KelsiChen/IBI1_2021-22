import re

input=open("Saccharomyces_cerevisiae.R64-1-1.cdna.all 2.fa")
output=open("cut_genes.fa","w")

NAME=[]
LINE=[]

i=0
for l in input:
	if l.startswith(">"):
		name=">"+re.findall(r"gene:(\w+)",l)[0]
		NAME.append(name)
		i=i+1
	if not l.startswith(">"):
		newline=l.strip("\n")
		if len(LINE) < i:
			LINE.append(newline)
		else:
			LINE[i-1]=LINE[i-1]+newline

LENGTH=[]

for i in range(len(LINE)):
	LENGTH.append(len(LINE[i]))

for i in range(len(NAME)):
	if len(re.findall("GAATTC",LINE[i])) !=0:
		output.write(NAME[i])
		output.write("")
		output.write(str(LENGTH[i]))
		output.write("\n")
		output.write(LINE[i])
		output.write("\n")

output.close()
	
