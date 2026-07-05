class Solution:
    def majorityElement(self, nums ):
        nums=sorted(nums)
        ans={}
        cnt=[]
        n=len(nums)
        for val in nums:
            if  val in ans:
                ans[val]+=1
            else:
                ans[val]=1
        for val1 in ans :
            if  ans[val1]>n//3:
                cnt.append(val1)  
        print(cnt)                  
        return cnt
object=Solution()
object.majorityElement([3,2,3])

        

        