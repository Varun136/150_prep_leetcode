""" 
DIFFICULTY = medium
"""
import bisect

def check_if_major_element(nums: list, target: int) -> bool:
    """
    check if target if the major element in nums
    using moore voting algorithm extension
    assumption : the major element will always lead in a sequence
    """

    count = 0
    for num in nums:
        if num == target:
            count += 1
        else:
            count -= 1
    return count > 0


def check_if_major_element_2(nums: list, target: int) -> bool:
    """
    check if target is the major element in nums
    using binary search on the left and right of the sequence
    """

    left = bisect.bisect_left(nums, target)
    right = bisect.bisect_right(nums, target)
    return (right-left) >= (len(nums) // 2)


if __name__ == "__main__":
    nums = [2,5,5,5,5,5,5,6,6]
    target = 5
    print(bisect.bisect_right(nums, 5))
    print(bisect_right_manual(nums, 5))
    # nums = [10,100,101,101]
    # target = 101
    print(check_if_major_element(nums, target))