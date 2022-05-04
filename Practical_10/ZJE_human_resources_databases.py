class Staff():
	def __init__(self,first_name,last_name,location,role):
		self.first_name=first_name
		self.last_name=last_name
		self.location=location
		self.role=role
	def print(self):
		print("staff name:",self.last_name,self.first_name,"location:",self.location,"role:",self.role)

Information=Staff(input("first_name:"),input("last_name:"),input("location:"),input("role:"))
Information.print()

#Example:
#Input:
#	first_name:Kai
#	last_name:Jiang
#	location:Zijingang Campus,Zhejiang University
#	role:PE Teacher
#Output:
#	staff name: Jiang Kai location: Zijingang Campus,Zhejiang University role: PE teacher	

#Note:People in China are used to putting the last name before the first name. Therefore, after all informations are inputted, this program first prints out staffs' last name, then prints out their first name. 
