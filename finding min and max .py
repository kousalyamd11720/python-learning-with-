arr=[2,5,23,1,9]

max=arr[0]
min=arr[0]

for i in arr:
    if (arr[i]>max):
        max=arr[i]
    if(min<arr[i]):
        min=arr[i]