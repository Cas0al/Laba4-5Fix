def y(x,eps,k):
    if abs(k-0.5*(k+x/k))>eps:
            return y(x,eps,0.5*(k+x/k))
    return 0.5*(k+x/k)

x=int(input())
eps=float(input())
print(y(x,eps,1))
