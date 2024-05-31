def sum_all(*args):
    print(*args)
    for i in args:
        print(i * 2)
print(sum_all(5,5))
print(sum_all(5,5,6,6,7,3,2,1))