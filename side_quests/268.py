""" 
QUESTION:
    Given an array nums containing n distinct numbers in the range [0, n], 
    return the only number in the range that is missing from the array.
"""


def get_the_missing_number(nums: list) -> int:
    """Get the missing number from the list
    sum of n natural number = n*(n+1) / 2
    """

    n = len(nums)
    calculated_sum = (n * (n+1)) // 2
    for num in nums:
        calculated_sum -= num
    
    return calculated_sum



if __name__ == "__main__":
    nums = [9,6,4,2,3,5,7,0,1]
    print(get_the_missing_number(nums))