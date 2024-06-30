""" 
    Difficulty = easy
"""

def max_profit(nums: list) -> int:
    """Returns the maximum profit that can be optained by buying and then selling the stock"""

    # Cannot generate profit because cannot sell.
    if len(nums) <= 1: 
        return 0

    buy = nums[0]
    profit = 0

    for num in nums:
        if (num - buy) > profit:
            profit = (num - buy)
        
        if num < buy:
            buy = num

    # return 0 if no profite generated.
    return profit if profit > 0 else 0 



if __name__ == "__main__":
    nums = [9999,10000]

    print(max_profit(nums))