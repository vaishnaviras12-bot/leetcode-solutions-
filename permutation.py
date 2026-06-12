#permutation
result = []
def getpermutation(arr,index):
    if index == len(arr):
        result.append(arr[:])
        return result
    for i in range(index,len(arr)):
        arr[index],arr[i] = arr[i],arr[index]
        getpermutation(arr,index+1)
        arr[index],arr[i] = arr[i],arr[index]
#example-
getpermutation([1,2,3],0)
print(result)