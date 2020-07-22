def fibb(n):
    x = 0
    y = 1
    if n==1:
        return (x)
    if n==2:
        return (y)
    else:
        return fibb(n-1) + fibb(n-2)
n = int(input("Enter the value:"))
a = fibb(n)
print(a)