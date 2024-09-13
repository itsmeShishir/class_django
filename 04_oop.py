# oop -> object oriented programming
# class, object, 
# attribute, method, constructor, 
# 4 pillars of oop 
# inheritance, polymorphism, encapsulation, abstraction

#OOP -> 

#class -> blueprint of the class
class MyClass():
    a = 10

    def __init__(self, name, age):
        self._name = name
        self.__age = age

    #instance methods
    
    #class methods
    @classmethod
    def classData(cls):
        print(cls.a)
    @staticmethod
    def staticData():
        print(f"Hello ")
    
    def get_age(self):
        return {self.__age}

class subClass(MyClass):
    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender
  

obj1 = subClass("shishir", 28, "male")
print(obj1)
print(obj1._name)
print(obj1.gender)
# obj1.printData()
obj1.classData()
obj1.staticData()


# print(obj1.a)
# obj2 = MyClass("Hari", 20)
# obj2.a = 30
# print(obj2.a)
# obj3 = MyClass()
# print(obj3)
# print(obj3.a)

# class okClass():
#     pass

# class helo(okClass):
#     def __init__(self, name):
#         self.name = okClass()



class subs():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def __str__(self):
        return f"my name is {self.name} and my age is {self.age} and gender is {self.gender}"
    
    def __len__(self):
        return len(self.name)
    
ok = subs("shishir", 28, "male")
print(obj1)
print(ok)
print(len(ok))
