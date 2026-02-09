#function in python
#function is a block of code used to perform particular task 
def func():  #def --- keyword    #func--name of the function   #()--we can pass the parameters here 
    print("hello")    #block of code we have to write here 
func()               #calling the function to execute 


#example 1
#we create a function sub() using the def keyword, which calculates the difference between two numbers.

def sub(x,y):
    return (x-y)
x=3
y=4
res=sub(x,y)
print(res)


#example 2
#we define a user-defined function fun() using the def keyword. 
# #The function takes a parameter n and prints the prime numbers upto n

def prime(n):
    for i in range(1, n + 1 ):
        count = 0
        for j in range(1, i + 1 ):
            if i%j == 0:
                count=count+1
        if  count == 2:
            print(i)

prime(10)


#the function takes a parameter n and print first n prime numbers

def first_n_prime(n):
    count=0
    num=2

    while count<n:
        divisor_count=0
        for i in range (1,num+1):
            if num % i == 0:    
                divisor_count+=1
        if divisor_count == 2:  
            print(num)
            count+=1
    
        num+=1

first_n_prime(10)

