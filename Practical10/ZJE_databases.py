#Create the class
class Staff(object):
  def __init__(self, name, location, role):
    self.name = name
    self.location = location
    self.role = role
#I created a function called information to show the basic information.
  def information(self):
    print("Name:",self.name,"Location:",self.location,"Role:",self.role)

#I used 2 examples
#Example 1:
staff1=Staff("Rob Young","Edinburgh","Faculty")
staff1.information()
#Result:
#Name: Rob Young Location: Edinburgh Role: Faculty
#Example 2:
staff2=Staff("Wang Yufen","International Campus","Leadership")
staff2.information()
#Result:
#Name: Wang Yufen Location: International Campus Role: Leadership
