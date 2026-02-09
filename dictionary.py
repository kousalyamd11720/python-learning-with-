# dictionary

data={"name":"kousalya","age":23,"profession":"SE","isworking":True} # dictionary is used to store the data in key value pairs where we can acces the values using the key not by index

print(data)

#creating the dictionary

#using the {} brackets as mentioned above
# using the dict function
dic=dict(name="abc", age=23)
print(dic)

# adding the values to the dictionary
data["studying"]=False
print(data)

#updating using the name of the key
data["name"]="kouu"
print(data)

#removing the dictionary items

# using the del we can del the item using its key
del data["studying"]
print(data)
                                                            

# pop() it will delete the key aand return  value 
val=data.pop("age")
print(val)
print(data)

#clear() will delete all the items 
#data.clear()


#popitem() remove and returns the last key-value pair
key,val = data.popitem()
print(key,val)
print(data)

#iteration using the key() ,value() ,both
print("for loop to itirate ")
for key in data:
    print( key)
    # for printing the values we need to mention the variable.values
for value in data.values():
    print(value)
# for printing both key and values
for key,value in data.items():
    print(key,value)