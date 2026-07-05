nums=[1,2,3,4,8,9]
target=7
ans={}
def two_sum(nums,target):
    for i in range(len(nums)):
        if target -nums[i] in ans:
            return [ans[target-nums[i]],i]
        ans[nums[i]]=i
    return []
print(two_sum(nums,target))
