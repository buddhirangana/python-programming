class Person:
    def _init_(self, title="default_title"):
        self._name = None
        self.title = title
    def talk(self, words):
        print("talk 1")
    def talk(self, words):
        print("talk 2")

class Employee(Person):
    def _init_(self,id,title):
        super()._init_(xx)
        self.id = id

person1 = Person ()
person1.talk("Hello")

person2 = Person("Professor")
print (person2.title)
