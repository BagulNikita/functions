"""write a function that tasks variable number of arguments and return 
their sum"""

def sum_all(*args):
    print(*args)
    for i in args:
        print(i * 2)
    

print(sum_all(5,2))
print(sum_all(5,5,6,6,7,3,2,1))
print(sum_all(5,5,5,6,6,6,7,7,3,9,2,1))