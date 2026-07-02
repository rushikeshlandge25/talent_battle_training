add=0
nums=[-2,1,-3,4,-1,2,1,-5,4]
for i in range(len(nums)):
    add+=nums[i]
    if add<0:
        add=0
print(add)

