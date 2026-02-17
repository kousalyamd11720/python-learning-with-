#four pillars of OOPs
#inheritance -- it allows to access the parent class properties and methods inside the child class 
class animal:
    def __init__(self,name):
        self.name=name 

    def info(self):
        print(f"my pet is {self.name}")

class dog(animal):
    def sound(self):
        print(f"our {self.name} is barking")

d1=dog("tommy")
d1.info()  #accessing the parent class method through the child class object
print(d1.name)




#super() function 
# this is the function used in the child class to acces the parent class methods
#If a child class overrides the constructor without using super(), the parent class’s attributes won’t be initialized, which can lead to errors:
class people:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class emp(people):
    def __init__(self,name,age,email):
        super().__init__(name,age)#here we inheriting the parent calss constructor variables name and age 
        self.email=email
    def __str__(self):
        return (F"i am  {self.name} and age is {self.age} with the employee email {self.email}")

e1=emp("kousalya",23,"kousalyamd@gmail.com")
print(e1)



#there are different types of inheritance 
# 1. single inhertitance --  child class inheriting from only one parent class 

class people:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class emp(people):
    def __init__(self, name ,age ,id):
        super().__init__(name,age)
        self.id=id
    def show_id(self):
        print(f"{self.name} id is {self.id}")

obj=emp("kousalya",23,21)
print(obj.name,obj.age,obj.id)
obj.show_id()


# 2.Multiple inheritance -- single child class inheriting from the multiple parent class
class employe:
    def __init__(self,name):
        self.name = name 

class team:
    def __init__(self,team_name):
        self.team_name= team_name

class project(employe,team):
    def __init__(self,name,team_name,project_name):
        #super().__init__(name,team_name) #here we cannot use the super because super() follows MRO it will call only employee but employee doen't call team 
        employe.__init__(self,name)
        team.__init__(self,team_name)
        self.project_name=project_name

    def prj_detail(self):
        print(f"{self.name} is in the {self.team_name} and eorking under the project {self.project_name}")

project1=project("kousalya","AI innovation","RAG chatboot")
project1.prj_detail()

#3.multilevel inheritance -- the class is derived from the another derived class (like a chain)

class people:
    def __init__(self,name):
        self.name = name
    
class employe(people):
    def __init__(self,name,id):
        super().__init__(name)
        self.id = id
        print(f"the person {self.name} have id {self.id}")

class manager(employe):
    def __init__(self,name,id,role):
        super().__init__(name,id)
        self.role=role
    def proff(self):
        
        print(f"the person with name {self.name} have a id {self.id} working as {self.role}")

man=manager("kousalya",23,"manager")
man.proff()

#4.Hierarchical Inheritance --  multiple child class inheriting from the same parent class

class person:
    def __init__(self,name):
        self.name = name
    
class employe(person):
    def role(self):
        print(f"{self.name} is working as a employe in the company")

class intern(person):
    def role(self):
        print(f"{self.name} is an intern in this company")

employeobj=employe("kousalya")
employeobj.role()
internobj=intern("jonny")
internobj.role()


#5.Hybrid inheritance -- combination of more than one inheritance 
class Person:
    def __init__(self,name):
        self.name=name

class employe(Person):
    def role(self):
        print(f"{self.name} is a employee ")

class project:
    def __init__(self,project_name):
        self.project_name=project_name
    
class teamlead(employe,project):
    def __init__(self,name,project_name):
        employe.__init__(self,name)
        project.__init__(self,project_name)
        

    def details(self):
        print(f"{self.name} handiling the team in project{self.project_name}")

t1=teamlead("kousalya","innovation")
t1.details()
    