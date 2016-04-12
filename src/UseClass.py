'''
Created on 2016年4月1日

@author: Yo
'''
class Person:
    def SetName(self,name):
        self.name=name
    @staticmethod
    def GetName(self):
        return self.name

    def __init__(self,name="Natasha"):
        self.name=name
        #print("Create Person")
    def __str__(self):
        print("This man's name is %s"%(self.name))
    
class Manager(Person):
    def __init__(self,name="Harry"):
        #super().__init__();
        Person.__init__(self)
        print(self.name)
        self.name=name
        print(self.name)
        
