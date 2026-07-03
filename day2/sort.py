nums=[2,1,0,1,2,0,1,2,0,1,2]
low=0
mid=0
high=len(nums)-1
while mid<=high:
    if nums[mid]==0:
        nums[low],nums[mid]=nums[mid],nums[low]
        low+=1
        mid+=1
    elif nums[mid]==1:
        mid+=1
    elif nums[high]==0:
        nums[low],nums[high]=nums[high],nums[low]
        low+=1
        high-=1
    elif nums[high]==1:
        nums[mid],nums[high]=nums[high],nums[mid]
        mid+=1
        high-=1     
    elif nums[mid]==2:
        nums[mid],nums[high]=nums[high],nums[mid]
        high-=1
        mid+=1
print(nums)