def reverse(nums: list, start: int, end: int) -> None:
    """
    Reverses the given array nums
    """

    if start >= end:
        return 
    if len(nums) <= 1:
        return
    
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
    return

def rotate_array(nums: list, k: int) -> None:
    """
    Rotate the given array nums to right k times
    Time complexity -> O(n)
    Space complexity -> O(1)
    """

    if len(nums) <= 1:
        return
    
    if k >= len(nums):
        k = k % len(nums)
    
    reverse(nums, 0, len(nums)-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, len(nums)-1)
    return

if __name__ == "__main__":
    nums = [1,2,3,4,5,6]
    k = 3
    rotate_array(nums, k)
    print(nums)