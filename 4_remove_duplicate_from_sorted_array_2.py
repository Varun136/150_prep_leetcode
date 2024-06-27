"""
    DIFFICULTY = "medium"
"""

def remove_duplicates(nums: list):
    if len(nums) <= 2:
        return len(nums)
    
    p = 2 # postion pointer
    # i is the index pointer

    for i in range(2, len(nums)):
        if nums[i] != nums[p-2]:
            nums[p] = nums[i]
            p += 1
    return p


if __name__ == "__main__":
    nums = [0,0,1,1,1,1,2,3,3]
    print(remove_duplicates(nums))

