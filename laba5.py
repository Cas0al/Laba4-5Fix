import random
def func(a,b):
    c=random.randint(a,b)
    print(c)
    n=int(input())
    while not(n==c):
        if n>c:
            print("Too much")
        elif n<c:
            print("Too low")
        n=int(input())
    print("Hell yeah")
a=int(input())
b=int(input())
func(a,b)
