#Create the class
class Chocolate(object):
  def __init__(self, money, price):
    self.money = money
    self.price = price
  def chocobar(self):
    number=self.money // self.price
    change=self.money % self.price
    change=round(change,3)
    print("The number of chocolate bar is",number,".","The change is",change,".")

#I used this as example, the money I have is 100, and the price is 7.5
c1= Chocolate(100,7.5)
c1.chocobar()
#The result is "The number of chocolate bar is 13.0 . The change is 2.5 ."


