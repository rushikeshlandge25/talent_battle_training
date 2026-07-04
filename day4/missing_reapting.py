nums=[1, 2, 5, 2, 3]
res={}
for i in range(len(nums)):
    if nums[i] in res:
        res[nums[i]]+=1
    else:
        res[nums[i]]=1
print(res)
missing=-1
reating=-1
for i in range(1,len(nums)+1):
    if i not in res:
        missing=i
    elif res[i]==2:
        reating=i
print("Missing number is:",missing)
print("Repeating number is:",reating)
