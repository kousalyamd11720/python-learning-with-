#sets 
sets={1,2,3,4,"kous",True,8}#boolean value won't support here 
print(sets)

#type castind
li=[1,3,5,56]
print(set(li))

#checking unique and immutable 

sets.add(4)#here it is not adding 4 because 4 is already present in the sets so no duplication is allowed 
print(sets)

#sets[1]=89 
# #we cannot replace the elemets because set is mutable only but we cannot change the single element

#print(sets[1])   we cannot access single value induvidually

a=frozenset(["a",12,234])  #frozen set accepts only one argument so we are passing as a list
print("frozensets",a) 
#here we cannot use the add() or remove() for the frozen set



#methods for the set 
#add()
sets.add("kouaslya")# inserting the element 
print(sets)

#union()
s1={1,3,4,5}
s2={1,4,6,7}

print(s1.union(s2))  #combines the values of set1 and set 2

#intersection()
print(s1.intersection(s2))# print the common values in both set 

#difference()
print(s1.difference(s2))  #returns a set containing elements that are in the first set but not in the second.

#clear() remove all the 