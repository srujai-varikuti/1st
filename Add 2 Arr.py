from numpy import *
arr = ([1,2,3,4,5])
arr1 = ([6,7,8,9,5])
arr2 = ([])
for i in range(len(arr)):
    for j in range(len(arr1)):
        x  = arr[i] + arr1[j]
        arr2.append(x)
        i+=1
        j+=1
    break
print(arr2)


