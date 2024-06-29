def first_occurence(nums: list, target: int) -> int:
    """Get the first occurence of a number with binary search"""
    left, right = 0, len(nums)-1
    index = -1

    while (left <= right):
        
        mid = (left + right) // 2
        if (nums[mid] == target):
            index = mid
            right = mid - 1
        else:
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
    return index

def last_occurence(nums: list, target: int) -> int:
    """Get the last occurence of a number with binary search"""
    left, right = 0, len(nums)-1
    result = -1
    while (left <= right):
        mid = (left + right) // 2
        if nums[mid] == target:
            left = mid + 1
        else:
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

    return result