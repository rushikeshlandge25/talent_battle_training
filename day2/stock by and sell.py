prices = [7, 10, 1, 3, 6, 9, 2]
min_pr =prices[0]
res=0


for i in range(1, len(prices)):
    
    
    min_pr = min(min_pr, prices[i])
    
    # Update result if we get more profit                
    res = max(res, prices[i] - min_pr)
print(res)

