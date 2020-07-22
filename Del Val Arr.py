from array import *

new_arr = array("i", [])
arr = array("i", [])
for i in range(5):
    x = int(input('Enter the value: '))
    new_arr.append(x)
print (new_arr)
k = 0
for j in new_arr:
    if k==2:
        k = k+1
        continue
    else:
        arr.append(j)
        k = k+1
print(arr)
