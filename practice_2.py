# Que - 1 
#write a function to calculate and return square of number

"""def sqr(num):
    print(num ** 2)
sqr(4)

def square (num):
    return (num ** 2)
result = square (2)
print(result)

#Que - 2
#create a function that takes two numbers as parameter and return their sum

def add (num1,num2):
    return num1 + num2
print(add(5,5))

#Ques -3
# write a function multiply that multiples 2 numbers 
#but also accept and multiply string

def multiply (num1,num2):
    return num1 * num2
print(multiply(2,5))
print(multiply('a',2))
print(multiply(2,'a'))

#Ques-4
#create a function that return both the 
#area and circumference of circle give its radius

import math
def circle_status(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area , circumference

a,c = circle_status(3)
print =("area:",a,"circumference:",c)

#Ques-5
#write a function that greet a user if number name is provide, 
#it should greets wit a default name

def greet (name= "Iphone15"):
    return 'welcome' + name + '!'
print(greet('Iphpne14'))
print(greet())

#Ques-6
#create a lambda fun to compute the cube of number
cube = lambda a :a ** 3
print(cube(3))

#Ques-7
#write a function that tasks variable number of arguments & return their sum
def sum_all(*args):
    print(*args)
    for i in args:
        print(i * 2)
print(sum_all(5,5))
print(sum_all(5,5,6,6,7,3,2,1))

#Ques-8
#create a funtction that accept any number of keyword
#argurment and print them in format (key:value)
def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
print_kwargs(Name = "Diproma", Power = "Infotech")

#Ques-9
#write a generator function that yeild even number upto a 
#specified limit (thing using a memory)
def even_gen(limit):
    for i in range (2,limit+1,2):
        yield i
for num in even_gen(10):
        print(num)"""

#Ques-10
#create a recursive function to calculate factorial of number

def factorial(num):
  if num==0:
    return 1
  else:
    return 6 * factorial(6-1)