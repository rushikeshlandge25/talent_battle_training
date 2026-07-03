# Initial Inputs
arr1 = [1, 5, 9, 10, 15, 20]
arr2 = [2, 3, 8, 13]

# Step-by-Step Swap Executions:
# Compare arr1[5]=20 and arr2[0]=2  -> 20 > 2  -> Swap! -> arr1=[1,5,9,10,15,2] , arr2=[20,3,8,13]
# Compare arr1[4]=15 and arr2[1]=3  -> 15 > 3  -> Swap! -> arr1=[1,5,9,10,3,2]  , arr2=[20,15,8,13]
# Compare arr1[3]=10 and arr2[2]=8  -> 10 > 8  -> Swap! -> arr1=[1,5,9,8,3,2]   , arr2=[20,15,10,13]
# Compare arr1[2]=9  and arr2[3]=13 -> 9 <= 13 -> Break!

# Internal Array Sorting:
# Sort arr1 -> [1, 2, 3, 5, 8, 9]
# Sort arr2 -> [10, 13, 15, 20]

# Final Outputs
arr1 = [1, 2, 3, 5, 8, 9]
arr2 = [10, 13, 15, 20]

ans=[]
ar1=0
ar2=0
i=0
while ar1<len(arr1):
    if arr1[ar1]<arr2[ar2]:
        ans.append(arr1[ar1])
        ar1+=1
    else:
        ans.append(arr2[ar2])
        ar2+=1
    i+=1
while ar2<len(arr2):
    ans.append(arr2[ar2])
    ar2+=1
for i in range(len(arr1)):
    arr1[i]=ans[i]
print("Merged Sorted Array:", arr1)
for i in range(len(arr2)):
    arr2[i]=ans[i+len(arr1)]
print("Remaining Elements in arr2:", arr2)
