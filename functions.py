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



#passing function as an argument to another function 

def fun(func,arg):
    return func(arg)

def square(x):
    return x*x

a=6
result=fun(square,a)
print(f"square of value {a} is ",result)


# *args -- it allows the function to accept multiple arguments and it will be treated as a tuple inside the function

def func(*args):
    print("passing the multiple number of inputs")
    for i in args:
        print(i)

func(1,2,3,4,5)

# **kwargs -- lets the function to accept any number of keywords as argumnets and collect it as a dictionary 

def func(**kwargs):
    for k,v in kwargs.items():
        print(k,v)

func(name="kousalya",age=23)


# TYPES OF FUNCTION ARGUMENTS
#1.DEFAULT ARGUMENTS
def func(x,y=10):
    print(x,y)
func(5)

#2.keyword arguments ---- order doesn't matter here 
def func(x,y):
    print(x,y)
func(y=21,x=19)

#3. postition argument 
def func(x,y):
    print("passing position arg",x,y)
func(10,20)

#4.arbitary arguments(*) (**)

#lambda function --- lambda is a keyword used to create anonoymous fuction(a function without a name ) 

a= lambda x:x*x
print(a(5))

#return  statement --- return is a keword which will end the execution of the function and return the values
#it will return any type of datatype , for multiple values it returns tuples()

def func(a,b):
    return 
print(func(2,4))


#pass by value and pass by reference 
#but in the python everythng is pass by refeefrence but changes depends on the type of object

#immutable = pass by value -- int , float, string, tuple

def func(x):
         x=x+10
         return x
x=10
print("original value",x)
print("modified in the function",func(x))


#mutable = pass by reference -- list , set , dict

def func(list):
    list.append(4)
    return list

original_list=[1,2,3]
print("orignal value",original_list)
print("modified value",func(original_list)) #here it is affected which is changed inside the resume



#recursive function -- a function call by itself is called recursive function 

def factorial(n):
    if n==0^n==1:
        return 1
    else:
        return n*factorial(n-1)
    
n=4
print(f"factorial of {n} is",factorial(n))