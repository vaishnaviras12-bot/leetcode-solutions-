nums=[1,2,3,4,5,6]
n=len(nums)-1
cost=0
while (n>=0):
    cost= nums[n]+nums[n-1]
    n=n-3
print(cost)


