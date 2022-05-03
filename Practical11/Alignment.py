import re

#Import the data. 
with open("C:\\Users\\50100\\Desktop\\Practical11\\DLX5_human.fa") as fa:
    human = fa.read()

#Extract the amino acid sequence.
human_re = re.findall(r'\n(\S+)', human)
human_re = str(human_re)
seq_human=[]
for line in human_re:
    line= line.replace('[','')
    if not line.startswith(']'):
        seq_human += line

#delete useless punctuation.
del seq_human[0]
del seq_human[-1]

#Repeat moves above to get data from the other files. 
with open("C:\\Users\\50100\\Desktop\\Practical11\\DLX5_mouse.fa") as fa:
    mouse = fa.read()

mouse_re = re.findall(r'\n(\S+)', mouse)
mouse_re = str(mouse_re)

seq_mouse=[]
for line in mouse_re:
    line= line.replace('[','')
    if not line.startswith(']'):
        seq_mouse += line

del seq_mouse[0]
del seq_mouse[-1]

with open("C:\\Users\\50100\\Desktop\\Practical11\\RandomSeq(1).fa") as fa:
    random = fa.read()

random_re = re.findall(r'\n(\S+)', random)
random_re = str(random_re)

seq_random=[]
for line in random_re:
    line= line.replace('[','')
    if not line.startswith(']'):
        seq_random += line

del seq_random[0]
del seq_random[-1]

#Set the initial number of identical amino acid to zero
edit_distance_human_mouse = 0
edit_distance_human_random = 0
edit_distance_mouse_random = 0


#calculate the number of identical amino acid
for i in range(len(seq_mouse)):       #compare each amino acid
    if seq_mouse[i]!=seq_human[i]:
        edit_distance_human_mouse += 1 #add a score 1 if amino acids are different

for i in range(len(seq_human)):       
    if seq_random[i]!=seq_human[i]:
        edit_distance_human_random += 1 

for i in range(len(seq_random)):    
    if seq_random[i]!=seq_mouse[i]:
        edit_distance_mouse_random += 1


#culcalate the percentage of identical amino acid in the three comparisons
hm= edit_distance_human_mouse/len(seq_mouse)    
hm= (1-hm)*100
hr= edit_distance_human_random/len(seq_human)
hr=(1-hr)*100
mr= edit_distance_mouse_random/len(seq_random)
mr=(1-mr)*100


print ('The number of different amino acids between human and mouse is',edit_distance_human_mouse)
#The number of different amino acids between human and mouse is 10
print ('The percentage of identical amino acids between human and mouse is',hm,'%')
#The percentage of identical amino acids between human and mouse is 96.53979238754326 %
print ('The number of different amino acids between human and random is',edit_distance_human_random)
#The number of different amino acids between human and random is 281
print ('The percentage of identical amino acids between human and random is',hr,'%')
#The percentage of identical amino acids between human and random is 2.768166089965396 %
print ('The number of different amino acids between mouse and random is',edit_distance_mouse_random)
#The number of different amino acids between mouse and random is 280
print ('The percentage of identical amino acids between mouse and random is',mr,'%')
#The percentage of identical amino acids between mouse and random is 3.114186851211076 %

#The mouse sequence is 3.114186851211076 % similar to the random sequence.
#The human sequence is 2.768166089965396 % similar to the random sequence.

#Type in the amino acid list and BLOSUM62 score matrix.
amino_acid=['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V','B','Z','X','*']

BLOSUM62 = [
            [ 4, -1, -2, -2,  0, -1, -1,  0, -2, -1, -1, -1, -1, -2, -1,  1,  0, -3, -2,  0, -2, -1,  0, -4],
            [-1,  5,  0, -2, -3,  1,  0, -2,  0, -3, -2,  2, -1, -3, -2, -1, -1, -3, -2, -3, -1,  0, -1, -4],
            [-2,  0,  6,  1, -3,  0,  0,  0,  1, -3, -3,  0, -2, -3, -2,  1,  0, -4, -2, -3,  3,  0, -1, -4],
            [-2, -2,  1,  6, -3,  0,  2, -1, -1, -3, -4, -1, -3, -3, -1,  0, -1, -4, -3, -3,  4,  1, -1, -4],
            [ 0, -3, -3, -3,  9, -3, -4, -3, -3, -1, -1, -3, -1, -2, -3, -1, -1, -2, -2, -1, -3, -3, -2, -4],
            [-1,  1,  0,  0, -3,  5,  2, -2,  0, -3, -2,  1,  0, -3, -1,  0, -1, -2, -1, -2,  0,  3, -1, -4],
            [-1,  0,  0,  2, -4,  2,  5, -2,  0, -3, -3,  1, -2, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1, -4],
            [ 0, -2,  0, -1, -3, -2, -2,  6, -2, -4, -4, -2, -3, -3, -2,  0, -2, -2, -3, -3, -1, -2, -1, -4],
            [-2,  0,  1, -1, -3,  0,  0, -2,  8, -3, -3, -1, -2, -1, -2, -1, -2, -2,  2, -3,  0,  0, -1, -4],
            [-1, -3, -3, -3, -1, -3, -3, -4, -3,  4,  2, -3,  1,  0, -3, -2, -1, -3, -1,  3, -3, -3, -1, -4],
            [-1, -2, -3, -4, -1, -2, -3, -4, -3,  2,  4, -2,  2,  0, -3, -2, -1, -2, -1,  1, -4, -3, -1, -4],
            [-1,  2,  0, -1, -3,  1,  1, -2, -1, -3, -2,  5, -1, -3, -1,  0, -1, -3, -2, -2,  0,  1, -1, -4],
            [-1, -1, -2, -3, -1,  0, -2, -3, -2,  1,  2, -1,  5,  0, -2, -1, -1, -1, -1,  1, -3, -1, -1, -4],
            [-2, -3, -3, -3, -2, -3, -3, -3, -1,  0,  0, -3,  0,  6, -4, -2, -2,  1,  3, -1, -3, -3, -1, -4],
            [-1, -2, -2, -1, -3, -1, -1, -2, -2, -3, -3, -1, -2, -4,  7, -1, -1, -4, -3, -2, -2, -1, -2, -4],
            [ 1, -1,  1,  0, -1,  0,  0,  0, -1, -2, -2,  0, -1, -2, -1,  4,  1, -3, -2, -2,  0,  0,  0, -4],
            [ 0, -1,  0, -1, -1, -1, -1, -2, -2, -1, -1, -1, -1, -2, -1,  1,  5, -2, -2,  0, -1, -1,  0, -4],
            [-3, -3, -4, -4, -2, -2, -3, -2, -2, -3, -2, -3, -1,  1, -4, -3, -2, 11,  2, -3, -4, -3, -2, -4],
            [-2, -2, -2, -3, -2, -1, -2, -3,  2, -1, -1, -2, -1,  3, -3, -2, -2,  2,  7, -1, -3, -2, -1, -4],
            [ 0, -3, -3, -3, -1, -2, -2, -3, -3,  3,  1, -2,  1, -1, -2, -2,  0, -3, -1,  4, -3, -2, -1, -4],
            [-2, -1,  3,  4, -3,  0,  1, -1,  0, -3, -4,  0, -3, -3, -2,  0, -1, -4, -3, -3,  4,  1, -1, -4],
            [-1,  0,  0,  1, -3,  3,  4, -2,  0, -3, -3,  1, -1, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1, -4],
            [ 0, -1, -1, -1, -2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2,  0,  0, -2, -1, -1, -1, -1, -1, -4],
            [-4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4,  1],]

#write the function to calculate the BLOSUM score.
def BLOSUM(a1,a2):
    score=0
    for i in range(len(seq_human)):
        index1=amino_acid.index(a1[i])
        index2=amino_acid.index(a2[i])
        score=score+BLOSUM62[index1][index2]   
    return score

#calculate the BLOSUM score
score_hm=BLOSUM(seq_mouse,seq_human)
score_hr=BLOSUM(seq_human,seq_random)
score_mr=BLOSUM(seq_mouse,seq_random)

#print out the BLOSUM score
print('The BLOSUM score between human and mouse is',score_hm)
#The BLOSUM score between human and mouse is 1490
print('The BLOSUM score between human and random is',score_hr)
#The BLOSUM score between human and random is -351
print('The BLOSUM score between mouse and random is:',score_mr)
#The BLOSUM score between mouse and random is -348


#From the progamme above, I can get the BLOSUM score, percentage of identical amino acid, and number of different amino acid.
#The BLOSUM score between human and mouse is 1490.
#The percentage of identical amino acids between human and mouse is 96.53979238754326 %
#The BLOSUM score between human and random is -351.
#The percentage of identical amino acids between human and random is 2.768166089965396 %
#The BLOSUM score between mouse and random is -348.
#The percentage of identical amino acids between mouse and random is 3.114186851211076 %
#I found that the human sequence and the mouse sequence are quite similar.
#Meanwhile, they are both quite different from the random sequence.
#I think that the similarity in amino acid sequences between human and mouse contribute to some similar structures in the two species.
#Moreover, perhaps evolution is the result of small changes in some amino acid sequences.
