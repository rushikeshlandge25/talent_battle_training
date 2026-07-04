nums=[1,1,2,2,3,4,4,5,5]
output=3
res={}
for i in range(len(nums)):
    if nums[i] in res:
        res[nums[i]]+=1
    else:
        res[nums[i]]=1
for i in res:
    if res[i]==1:
        print(i)