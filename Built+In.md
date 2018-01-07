
# Function Arguments

We can pass arbitrary number of arguments to a python fuction using *args as a function parameter


```python
# *args

def numbers(param1, *args):
    print (param1)
    print (args)
    
numbers(1,2,3,4,5)  
```

    1
    (2, 3, 4, 5)
    

>Passing default values to a function parameter, with this if we do not pass a agrument for that parameter it will take the default value instead. 


```python
# default

def name(x,y, food = 'Good'):
    print (food)

name(1,2)
name(1,2, 'Bad')    
    
```

    Good
    Bad
    

using __**kwargs__(keyword arguments) we can pass undefined named arguments to the function


```python
# **kwargs

def name(x,y,**kwargs):
    print (kwargs)

    
name(1,2)

name(1,2,name = 'sai')
```

    {}
    {'name': 'sai'}
    

> here kwargs is a dictionary object 

# Ternary operator


```python
a = 5

b = 1 if a>= 1 else 50

print (b)
```

    1
    

> This can be really useful when assigning values to the variables based on a condition and also results in less overall code 

# else

The else statement can also be used with while and for loops

In this case the else will be called if the output finishes normally


```python
# else

for i in range(10):
    if i == 111:
        print ("if 1")
        break
else:
    print ("else 1")
    
    

for i in range(10):
    if i == 1:
        print ("if 2")
        break
else:
    print ("else 2")    
```

    else 1
    if 2
    

> we can also use this with try and expect


```python
# else

i = 1

print ("first case:")

try:
    print (i/0)
except ZeroDivisionError:
    print ("impossible")
else:
    print ("No error")

    
print ("\nsecond case:") 
    
    
try:
    print (i/1)
except ZeroDivisionError:
    print ("impossible")
else:
    print ("No error")

```

    first case:
    impossible
    
    second case:
    1.0
    No error
    


```python

```
