""" 
DIFFICULTY = medium
"""

def get_the_majority_elements(nums: list) -> list:
    """
    Get the majority element from nums which occur more than n/3 times
    note - If borth element occurs more than n/3 then only max 2 element willl be there
    """

    # Get the major 2 elements from nums
    count_1, count_2, candidate_1, candidate_2 = [0] * 4
    for num in nums:
        if candidate_1 == num:
            count_1 += 1
        elif candidate_2 == num:
            count_2 += 1
        elif count_1 == 0:
            candidate_1 = num
            count_1 += 1
        elif count_2 == 0:
            candidate_2 = num
            count_2 += 1
        else:
            count_1 -= 1
            count_2 -= 1

    # Get the count of the major 2 elements
    count_1, count_2 = [0] * 2
    for num in nums:
        if num == candidate_1: count_1 += 1
        elif num == candidate_2: count_2 += 1

    # Check if the elelements occur more than n/3 times
    result = []
    if count_1 > len(nums) // 3: result.append(candidate_1)
    if count_2 > len(nums) // 3: result.append(candidate_2)

    return result


if __name__ == "__main__":
    nums = [1,2]
    print(get_the_majority_elements(nums))