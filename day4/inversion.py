arr = [6, 3, 5, 2,7]
output = 6
def count_inversions(arr):
    cnt=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                cnt+=1
    return cnt
print(count_inversions(arr))        



    