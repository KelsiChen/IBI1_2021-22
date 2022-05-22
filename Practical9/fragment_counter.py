seq = 'ATGCAATCGACTACGATCAATCGAGGGCC'
#First,figure out the number of EcoRI sequence, number of fragment is number of sequence plus one.
fragment=seq.count('GAATTC')+1
print("The number of fragments generated is", fragment)
