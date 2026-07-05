# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
m = 3
n = 2
def unique_path(m,n):
    dp=[[-1]*(n) for i in range(m)]
    return unique(m-1,n-1,dp)
def unique(m,n,dp):
    if m==0 and n==0:
        return 1
    if m<0 or n<0:
        return 0
    if dp[m][n]!=-1:
        return dp[m][n]
    left=unique(m-1,n,dp)
    right=unique(m,n-1,dp)
    dp[m][n]=left+right
    return dp[m][n]
print(unique_path(m,n))
