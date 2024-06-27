"""
    DIFFICULTY = "easy"
"""

# my approach.
def merge_sorted_array(nums1: list, nums2: list, m: int, n: int):
    i, j, k = m-1, n-1, m+n-1  # 0(1)

    while (i >= 0) and (j >= 0) and (k >= 0):  # 0(i+j)
        if nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i-=1
        else:
            nums1[k] = nums2[j]
            j-=1
        k-=1
    while i>=0:  # 0(i)
        nums1[k] = nums1[i]
        i-=1
        k-=1
    
    while j>=0:  # 0(j)
        nums1[k] = nums2[j]
        j-=1
        k-=1

    
    # the overall time complexity
    # 0(1) + 0(i+j) + 0(i) + 0(j) = 0(i+j) = 0(m+n)
    return True


# leetcode better whie loop usage.
# submitted to leet code
def merge_sorted_array2(nums1: list, nums2: list, m: int, n: int):
    if not nums:
        return 0

    k = 0
    nums.sort()  # Ensure the list is sorted

    for i in range(1, len(nums)):
        if nums[i] != nums[k]:
            k += 1
            nums[k] = nums[i]
    
    return k + 1
    

if __name__ == "__main__":

    nums1, m = [1,2,3,0,0,0], 3
    nums2, n = [4,5,6], 3
    merge_sorted_array(nums1, nums2, m, n)
    print(nums1)