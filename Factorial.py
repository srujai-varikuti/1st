def fact(n):
    a = 1
    for i in range(1,n+1):
        a = a*i
        i=i+1
    return a
n = int(input('Enter the value: '))
x = fact(n)
print(x)