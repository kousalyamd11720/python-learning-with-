#tuple  
#it is immutable ordered collection of elements similar like list but cannot change after creation of list 
tup=('kous',1,4.5,True)

print(tup)

#creating the tuple
#using the () as mentioned above
#using the tuple() 
li=[1,2,3,4,4]
tupl=tuple("kous")
print(tupl)
print(tuple(li))

#nested tuple
tup1=(2.4,2.4,254)
tup2=("sbfs","abc")
tup3=(tup1,tup2)
print(tup3)

#creating the tuple with repetation
tupr=("kousalya",)*3
print(tupr)


#accessing the tuple using 
#indexing 
print(tup[3])

#slicing
print(tup[1:3])
print(tup[:4])#start from starting 
print(tup[::-1])#reversing the tuple

#concatenation
print(tup1+tup2)

#unpacking the tuple 
a,b,c,d =tup #we should mention same number of varibale as items int he tuple
print("unpacking 1",a)
print(b)

#for unpacking multiple items 
a,*b,c=tup
print("unpacking multiple items",b)
#deleting the tuples we cannot delete only one tuple because it is immuatable
#note:- after deleting the tupe if we try to print we will get an error 

del tup
print(tup)
