""" 
QUESTION:
    Given an array arr, replace every element in that array with the greatest element 
    among the elements to its right, and replace the last element with -1.
"""


def replace_element(nums: list) -> list:
    """Replace all the elements with greatest element from its right"""
    
    n = len(nums)
    max_element = nums[-1]
    for i in range(n-2, -1, -1):
        if nums[i] < max_element:
            nums[i] = max_element
        else:
            max_element, nums[i] = nums[i], max_element
    
    nums[-1] = -1
    return nums


if __name__ == "__main__":
    nums = [17,18,5,4,6,1]
    print(replace_element(nums))