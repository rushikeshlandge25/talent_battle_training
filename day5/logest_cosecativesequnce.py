class Solution:
    def longestConsecutive(self, nums):
        
        nums=list(set(nums))
        if nums==[]:
            return 0
        nums=sorted(nums)
        cnt=1
        maxi=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                    cnt+=1
                    maxi=max(cnt,maxi)
            else:
                cnt=1
        print(maxi)
obj=Solution()
obj.longestConsecutive([100,4,200,1,3,2])