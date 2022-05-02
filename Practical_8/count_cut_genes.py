import re

file=input("file name:")
input=open(file)
output=open("count_cut_genes.fa","w")

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

CUT=[]
for i in range(len(LINE)):
	enzyme_cut=re.findall('GAATTC',LINE[i])
	fragment_count=len(enzyme_cut)+1
	CUT.append(fragment_count)

for i in range(len(NAME)):
	if len(enzyme_cut) !=0:
		output.write(NAME[i])
		output.write("")
		output.write(str(CUT[i]))
		output.write("\n")
		output.write(LINE[i])
		output.write("\n")

output.close()
	

