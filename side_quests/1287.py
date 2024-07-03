""" 
    Given an integer array sorted in non-decreasing order, there is exactly one integer 
    in the array that occurs more than 25% of the time, return that integer.
"""

def find_special_integer(nums: list) -> int:
    """Find the element that appears more than 25% in the array"""

    n = len(nums)
    if n == 1:
        return nums[0]
    
    j = 0
    count = 0
    for i in range(n):
        if nums[i] != nums[j]:
            count = 1
            j = i
        else:
            count += 1
        
        if count > n//4:
            return nums[i]
    
    return -1


if __name__ == "__main__":
    nums = [1,2,2,6,6,6,6,7,10]
    print(find_special_integer(nums))
