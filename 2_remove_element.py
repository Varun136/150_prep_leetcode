"""
    DIFFICULTY = "easy"
"""

def remove_element(nums: list, val: int):
    k = 0

    for i in range(len(nums)): # 0(n=len(nums))
        if nums[i] != val:
            if i != k: 
                nums[k] = nums[i]
            k += 1

    # time complexity is 0(n) 
    return k


if __name__ == "__main__":

    nums = [0,1,2,2,3,0,4,2]
    val = 2
    nums2, n = [4,5,6], 3
    print(remove_element(nums, val))
    