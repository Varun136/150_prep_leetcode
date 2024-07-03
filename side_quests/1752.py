""" 
QUESTION:
    Given an array nums, return true if the array was originally sorted in non-decreasing order, 
    then rotated some number of positions (including zero). Otherwise, return false.
    There may be duplicates in the original array.
    Note: An array A rotated by x positions results in an array B of the same length such that 
    A[i] == B[(i+x) % A.length], where % is the modulo operation.
"""


def check_is_rotated(nums: list) -> bool:
    """Check to see if array is sorted even if it is 
    rotated"""

    count = 0 # count how many times the sort order was disordered
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            count += 1
    
    if nums[0] < nums[-1]:
        count += 1
        
    # is sort order is disoredered more than once then False
    return count <= 1 


if __name__ == "__main__":
    nums = [3,4,5,1,2]
    print(check_is_rotated(nums))

    nums1 = [2,1,3,4]
    print(check_is_rotated(nums1))
