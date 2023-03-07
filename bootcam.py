f=open ("Menu.txt","w",encoding="utf-8") 
f.write("Lütfen bir pizza tabanı seçiniz:\n1:Klasik\n2:Margherita\n3:Pepperoni\n4:Gennaro\n ve seçeceğiniz sos\n"
"5:Zeytin\n6:Manta\n7:Et\n8:Mısır\n9:Keçi peyniri")
f.close()

f = open("Menu.txt", "r",encoding="utf-8")
print(f.read())

class Pizza:
    def get_description(self):
        return self.__class__.__name__
    def get_cost(self):
        return self.__class__.cost

class Karışık(Pizza):
  cost=65 
  print("içindekiler:mantar, kaşar peyniri, domates, sucuk, salam ve sosis")  
class Margherita(Pizza):
  cost=87
  print("içindekiler:domates, mozarella, fesleğen")  
class Pepperoni(Pizza):
   cost=62
   print("içindekiler:mozarella, pepperoni, kekik")    
class Gennaro(Pizza):
  cost=84
  print("içindekiler: dilimlenmiş sucuk,mantar, mısır ")

class Decorator(Pizza):
   def _init_(self,pizza):
      self.pizza=pizza
      def get_cost(self):
       return self.component.get_cost() + \
         Pizza.get_cost(self)
   def get_description(self):
       return self.component.get_description() + \
         ' ' + Pizza.get_description(self) 
   
class Zeytin(Decorator): 
   cost=6
   def __init__(self, Pizza):
        Decorator.__init__(self, Pizza)
        
class Mantar(Decorator):
   cost=8
   def __init__(self, Pizza):
        Decorator.__init__(self, Pizza)

class Et(Decorator):
   cost=35
   def __init__(self, Pizza):
        Decorator.__init__(self, Pizza) 

class Mısır(Decorator):            
  cost=16
  def __init__(self, Pizza):
     Decorator.__init__(self, Pizza) 

class Keçipeyniri(Decorator):            
  cost=12
  def __init__(self, Pizza):
     Decorator.__init__(self, Pizza)             