def func(a,b):
    print("Введите число")
    n=int(input())
    while not(min(a,b)<=n<=max(a,b)):
        print("Введите число")
        n=int(input())
    print("Число угадано")
a=int(input())
b=int(input())
func(a,b)
