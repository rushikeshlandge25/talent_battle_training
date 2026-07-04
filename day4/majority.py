nums=[2, 2, 1, 1, 1, 2, 2]
candidate=None
cnt=0
# n=len(nums)
# print(n)
# for i in range(len(nums)):
#     if cnt==0:
#         candidate=nums[i]
#         cnt+=1
#     elif candidate==nums[i]:
#         cnt+=1
#     else:
#         cnt-=1
# print(candidate)
res={}
for i in range(len(nums)):
    if nums[i] in res:
        res[nums[i]]+=1
    else:
        res[nums[i]]=1
for val in res:
    if res[val]>len(nums)//2:
        print(val)