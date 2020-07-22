def count(input):
    i=j=0
    for a in input:
        if len(a)>5:
            i = i+1
        else:
            j = j+1
    return i,j
lst = input("Enter the names of the users: ")
input = lst.split(",")
x,y = count(input)
print ('Names with less than 5 char : {} and Names with more than 5 char : {}' .format(y,x))
