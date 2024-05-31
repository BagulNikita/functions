"""create a funtction that accept any number of keyword
argurment and print them in format (key:value)"""

def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
   
print_kwargs(name="Krishna", power="Ahire",enemy="BJP")


