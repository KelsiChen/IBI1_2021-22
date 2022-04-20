def cal(i):
    i=i.upper() #To turn data stored as lower cases into upper cases.
    res=str(i)
    count_all=len(res)
    count_A = res.count('A')
    percentage_A= count_A/count_all
    print("The percentage of A is",percentage_A*100,"%")
    count_T = res.count('T')
    percentage_T= count_T/count_all
    print("The percentage of T is",percentage_T*100,"%")
    count_C = res.count('C')
    percentage_C= count_C/count_all
    print("The percentage of C is",percentage_C*100,"%")
    count_G = res.count('G')
    percentage_G= count_G/count_all
    print("The percentage of G is",percentage_G*100,"%")


#Then input the sequence here
seq=input()
#I used "atcgggGATC" to test

#calculate the percentage with the function cal()
cal(seq)
#result:
#The percentage of A is 20.0 %
#The percentage of T is 20.0 %
#The percentage of C is 20.0 %
#The percentage of G is 40.0 %
