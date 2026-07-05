# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
nums = [1,0,-1,0,-2,2]
target = 0
def four_sum(nums, target):
    nums=sorted(nums)
    res=[]
    for i in range(len(nums)-3):
        if i>0 and nums[i]==nums[i-1]:
            continue
        for j in range (i+1,len(nums)):
            if j>i+1 and nums[j]==nums[j-1]:
                continue
            left=j+1
            right=len(nums)-1
            while left<right:
                total=nums[i]+nums[j]+nums[left]+nums[right]
                if total==target:
                    res.append([nums[i],nums[j],nums[left],nums[right]])
                    left+=1
                    right=right-1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                
                elif total<target:
                    left+=1
                else:
                    right-=1
                
              
    print(res)
    return res
print(four_sum(nums,target)) 