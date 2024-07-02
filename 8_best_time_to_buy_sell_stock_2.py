"""
    Difficult : Medium
"""

# Recursive approach with memmoisation
def decide_trade(nums: list, idx=0, can_buy=1, memo = {}) -> int:
    if len(nums) <= 1: 
        return 0
    
    if idx >= len(nums): # base conditions
        return 0
    
    # memoization
    if (idx+1, 0) not in memo:
        memo[(idx+1, 0)] = decide_trade(nums, idx+1, 0, memo)
    if (idx+1, 1) not in memo:
        memo[(idx+1, 1)] = decide_trade(nums, idx+1, 1, memo)


    if can_buy:
        profit = max( 
            memo[(idx+1, 1)], # move on to next day
            memo[(idx+1, 0)] - nums[idx] # buy the stock
        )
    else:
        profit = max( 
            memo[(idx+1, 0)], # move on to next day
            memo[(idx+1, 1)] + nums[idx] # sell the stock
        )
    
    return profit

# valley Peak approach
def decide_trade2(prices: list) -> int:
    """valley: local minima and peak: local maxima
    By ensuring to buy at local minima and sell at local maxima
    we ensure to capture every profit in the stcok upward movement
    Which will be the same as optimised buying and selling
    """
    n = len(prices) 
    if n <= 1:
        return 0
    
    profit = 0
    for i in range(1,n):
        if prices[i] > prices[i-1]:
            profit += (prices[i] - prices[i-1])
    
    return profit


if __name__ == "__main__":
    from datetime import datetime

    start = datetime.now()
    result = decide_trade2( [100, 180, 260, 310, 40, 535, 695])
    print(result)
    print(datetime.now()-start)
