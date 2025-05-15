# def maxprofit(prices):
#     l,r = 0,1
#     maxp = 0
#     while r < len(prices):
#         if prices[l] < prices[r]:
#             profit = prices[r]-prices[l]
#             maxp =max(maxp,profit)
#         else:
#             l =r
#         r+=1
#     return maxp                
         
# if __name__=="__main__":
#     stock=[10,22,5,75,65,80]
 
#     result = maxprofit(stock)
#     print(result)         


def maxprofit(prices):
    profit = 0
    for i in range(1,len(prices)):
        if prices[i] >prices[i-1]:
            profit += (prices[i]-prices[i-1])
    return profit

if __name__ =="__main__":
    stock=[10,22,5,75,65,80]
    result = maxprofit(stock)
    print(result)            