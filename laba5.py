import random
def func(a,b):
    c=random.randint(a,b)
    n=int(input())
    while not(n==c):
        if n>c:
            print("Перелёт")
        elif n<c:
            print("Недолёт")
        n=int(input())
    print("Число угадано")
a=int(input())
b=int(input())
func(a,b)
