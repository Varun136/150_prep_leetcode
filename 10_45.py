""" 
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i. In other words, 
if you are at nums[i], you can jump to any nums[i + j] where:
0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
"""


def get_min_jump(nums: list, idx: int, jump=0) -> int:
    """Get the minimum jumps required to get to the last element"""
    
    if len(nums) <= 0:
        return 0
    current = 0
    farthest = 0
    jump = 0
    for i in range(len(nums)):
        farthest = max(farthest, i + nums[i])
        if i == current:
            jump += 1
            current = farthest
            if current >= len(nums)-1:
                return jump
    return jump



if __name__ == "__main__":
    nums = [2,3,1,1,4]
    print(get_min_jump(nums, 0))