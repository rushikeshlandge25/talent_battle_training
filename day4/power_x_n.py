x=2
n =-10

def mypow(x,n):
    if n==0:
        return 1
    y= x*mypow(x,n-1)
    print(y)
    return y
if n<0:
    n=-n
    ans=1/mypow(x,n)
    print(ans)
else:
    print(mypow(x,n))
output=1024