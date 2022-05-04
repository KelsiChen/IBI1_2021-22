import re
DNA=input("DNA sequence=")
A_pattern=re.compile('[Aa]')
G_pattern=re.compile('[Gg]')
C_pattern=re.compile('[Cc]')
T_pattern=re.compile('[Tt]')

A_result=re.findall(A_pattern,DNA)
G_result=re.findall(G_pattern,DNA)
C_result=re.findall(C_pattern,DNA)
T_result=re.findall(T_pattern,DNA)

A_percentage=len(A_result)*100/len(DNA)
G_percentage=len(G_result)*100/len(DNA)
C_percentage=len(C_result)*100/len(DNA)
T_percentage=len(T_result)*100/len(DNA)

print("The percentage of A is",A_percentage,"%")
print("The percentage of G is",G_percentage,"%")
print("The percentage of C is",C_percentage,"%")
print("The percentage of T is",T_percentage,"%")

