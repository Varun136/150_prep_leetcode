"""
    DIFFICULTY = "easy"
"""

# Accepted by leetcode
# SC : 0(n) and TC : 0(n)
# did not notice the contrain of sorted array
def remove_duplicates(nums: list):
    """Removes the duplicate elements from the list"""

    unique_set = set() # stores the unique elements for check
    k = 0

    for i in range(len(nums)):
        if nums[i] not in unique_set:
            unique_set.add(nums[i])
            if i != k: nums[k] = nums[i]
            k += 1
    return k
    

# optimised solution in leet code with SC : 0(1)
def remove_duplicates(nums: list):
    k = 1

    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            if i != k: nums[k] = nums[i]
            k += 1
    return k

if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(remove_duplicates(nums))