total_money=input("total money:")
single_price=input("the price of one chololate bar:")


def number(total,single):
	number=int(float(total)/float(single))
	return number

chocolate_number=number(total_money,single_price)
money_left=float(total_money)-float(single_price)*chocolate_number

print("The number of chocolate bars the user is able to afford:",chocolate_number)
print("The money left:",money_left)

#Example:
#Input:
#	total money:120.6
#	the price of one chololate bar:2.3
#Output:
#	The number of chocolate bars the user is able to afford: 52
#	The money left: 1.0