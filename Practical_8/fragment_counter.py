import re

seq='ATGCAATCGACTACGATCAATCGAGGGCC'
enzyme_cut=re.findall('GAATTC',seq)
fragment_count=len(enzyme_cut)+1
print(fragment_count)

