def fib(n):
    x = 0
    y = 1
    if n>=1:
        if n == 1:
            print(x)
        else:
            print(x)
            print(y)
            for i in range(2,n):
                x,y= y,x+y
                i+=1
                print(y)
    else: print("Not Valid Input")
n = int(input('Enter the value: '))
fib(n)