#list

lists=[1,2,'q',3]   # creating the list using the square braces
a = list((1,2,3))   #  creating the list using the list constructor

print(lists)
print(a)

a=[2]*5     # creating the list with multiple elements
print(a)

print(lists[2])   # accesing the list elements through the index number


# adding elements into list 
#append adding only one element to the list at the end 
lists.append([10,24])   #considering this as one element 
print(lists)

# extend adding the multiple elements to the end of the string 
lists.extend([80,698])
print(lists)

#insert -- it will insert the element at the particular position 
lists.insert(3,96363)  #-- (position ,element)
print(lists)


#clear()--removes all the element from the list
lists.clear()
print(lists)


b=[2,5,'d',45]



#accessing the list 

print("accessing ",b[2])
print(b[:2])
print(b[1:4])
print(b[-1])    

# lists are mutubale --- update the list element using the index number
b[0]=3
print(b)



# Removing Elements from List
# remove(): Removes the first occurrence of an element.
b.remove(5)
print("removing from the list",b)

#pop(): Removes the element at a specific index or the last element if no index is specified.
b.pop(1)
print(b)

#del statement: Deletes an element at a specified index.
del b[0]
print(b)



#itirating over the loops
x=[2,5,27,35,'dfgu']

for item in x:
    print(item)