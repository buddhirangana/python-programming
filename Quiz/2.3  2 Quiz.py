class Person:
    def _init_(self, title="default_title"):
        self._name = None
        self.title = title
        
    def talk(self):
        print("I'm a person")
        
    def talk(self):
        print("I'm walking")

class Employee(Person):
    def _init_(self,id,title):
        super()._init_(title)
        self.id = id

    def talk(self):
        print("I'm an employee")

class SportsPerson(Person):
    def _init_(self,id,title):
        super()._init_(title)
        self.id = id

    def talk(self):
        print("I'm a sportsperson")

person1 = Person("p1")
person2 = Employee(1, "p2")
person3 = SportsPerson(2, "p3")

def check_talk(obj):
    obj.talk()

person2.talk()
    
