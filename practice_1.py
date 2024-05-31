#write a function to calculate and return the sqr of number

#def seq(number):
#    print(number**2)
#seq(5)

#function block of code that can be reusable as one or more time in program

#def square (number):
 #   return(number ** 2)
#result = square(4)
#print(result)

#write a function multiply that multiples two number
#and also accept the multiply string

#def multiply (num1,num2):
#    return num1*num2

#print(multiply(8,5))
#print(multiply(5,'a'))

#create a function that return both the area and circumference
#of circle given its radius

#import math
#def circle_sts(radius):
    
#    area = math.pi * radius **2
  #  circumference = 2 * math.pi * radius
  #  return area,circumference
#a,c=circle_sts(3)

#print("area:",a)
#print("circumference:",c)

#write a function that greet a user if name is provided 
#it should greet with a default name

#def greet (name="Iphone15"):
#    return "welcome," + name + "!"
##print(greet("Iphone14"))
#print(greet())

#create a lambda fun to compute the cube of lambda number

#cube = lambda a : a ** 3
#print(cube(4))

#write a function that takes variable number of arguments and 
#return their sum

#def sum_all (*args):
 #   return sum (args)
#print(sum_all(5,2))
#print(sum_all(5,5,6,6,7,3,2,1)).

#creat e a fun that accept any number of 
#keywords arrguments and print them in format (key:value)

#def print_kwargs(**kwargs):
#     for key,value in kwargs.items():
#        print(f"{key}:{value}")
   
#print_kwargs(name="Krishna", power="Ahire",enemy="BJP")

#write to generator function that yeild even number 
#upto specific limit (thng using memory)

def even_gen(limit):
    for i in range (2,limit+1,2):
        yield i
for num in even_gen(10):
        print(num)





