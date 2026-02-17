# class -- class is a cl=ollection of objects ,class is called the blueprint of the object

#creating a class

class student:
    name ="kousalya"

#creating the object for the class 
s1=student()
print(s1.name)#accessing the class varible using the object 


#__init__() -- it is a constucort in pu]ython which i sused to intiate the object attribute when we create the object for the class

class dog:
    species="barker"

    def __init__(self,name,age):
        self.name=name
        self.age=age
        pass
    def __str__(self):# this method we used to print the object in the form of string other wise if we try to print the object without using this method the object will be displayed like <__main__.dog object at 0x102edcfa0>
        return f"my dog name is {self.name} and age is {self.age}"

d1=dog("tommy",3)
print(d1.name)
print(d1.species)
print(d1)




