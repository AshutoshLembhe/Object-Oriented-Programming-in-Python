#class and objects

class Robot:
    def __init__(self,name,color, weight):
        self.name=name
        self.color=color
        self.weight=weight
        
    def introduce_self(self):
        print("my name is " + self.name)
      
        



r1=Robot("tom","red",30)
r2=Robot("jerry","blue",40)

r1.introduce_self()
r2.introduce_self()
