#reverseing the array
arr=[1,2,3,4,5]
rev=[]

for i in range(len(arr)-1,-1,-1):
        rev.append(arr[i])
    

print(rev)


#finding the max and min without usingt he max and min

max=arr[0]
min=arr[0]

for i in range(0,arr[i-1],1):
        if arr[i]>max:
                max=arr[i]
        else:
                min=arr[i]
print(max)
print(min)


#swaping the keyas and values in the dictionary

dic={"name":"kousalya","age":23}
new={}

for key,val in dic.items():
        new[val]=key

print(new)