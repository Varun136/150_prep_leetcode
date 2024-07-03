
# correct but ineffcient
def jump_game(nums: list, idx=0, memo_arr=None) -> bool:
    """Can check if we can jump to the last index from the position"""
    n = len(nums)

    if not memo_arr:
        memo_arr = [False] * n

    if n == 1:
        return True
    if idx == (n-1):
        return True
    if idx >= n or idx < 0:
        return False
    
    for i in range(1, nums[idx]+1):
        if not idx+i < n:
            continue

        if idx+i not in memo_arr:
            memo_arr[idx+i] = jump_game(nums, idx+i, memo_arr)
        if memo_arr[idx+i]:
            return True
    return False


# optimal solution 0(n)
def can_jump(nums: list) -> bool:
    """Jump game solution using the car-gasoline approah"""
    if len(nums) <= 1:
        return True 
    jump = 0
    for i in range(len(nums)):

        jump -= 1
        if jump == 0:
            if i == len(nums) - 1: return True
            jump = nums[i]
        elif (jump < nums[i]):
            jump = nums[i]

        if jump <= 0:
            return False
    
    return True


if __name__ == "__main__":
    nums = [2,0,0]
    print(can_jump(nums))