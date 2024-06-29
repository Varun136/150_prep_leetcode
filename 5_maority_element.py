"""
    DIFFICULTY = "easy"
"""

# simple approach
def get_major_element(nums: list) -> int:
    count_dict = {}
    
    for num in nums:
        if num not in count_dict:
            count_dict[num] = 1
            continue
        if count_dict[num] >= len(nums)//2:
            return num
        count_dict[num] += 1

# moore voting algorithm
def get_major_element_2(nums: list) -> int:
    """This algorithm is assuming that if an element has more than
    n//2 occurence in an array then it will laways be in lead"""
    count, candidate = 0, 0

    for num in nums:

        if count == 0:
            candidate = num
        
        if candidate == num:
            count += 1
        else:
            count -= 1
    return candidate


if __name__ == "__main__":
    print(get_major_element_2([2,2,1,1,1,2,2]))