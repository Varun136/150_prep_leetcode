""" 
Difficulty : medium
"""

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
    if (idx+2, 1) not in memo:
        memo[(idx+2, 1)] = decide_trade(nums, idx+2, 1, memo)


    if can_buy:
        profit = max( 
            memo[(idx+1, 1)], # move on to next day
            memo[(idx+1, 0)] - nums[idx] # buy the stock
        )
    else:
        profit = max( 
            memo[(idx+1, 0)], # move on to next day
            memo[(idx+2, 1)] + nums[idx] # sell the stock
        )
    
    return profit


if __name__ == "__main__":
    nums = [1]
    print(decide_trade(nums))
