""" 
QUESTION:
    Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
    You must implement a solution with a linear runtime complexity and use only constant extra space
"""


def check_single_number(nums: list) -> int:
    """Check the array for the number with only one ocurance.
    
    XOR means that if a number is xor twice it cancels out.
    logically if num not in once : add num to once.
    if added twice it cancels out as n^n = 0.
    """

    once = 0
    for num in nums:
        once ^= num 
    return once

def check_single_number_2(nums: list) -> int:
    """In the array all the element exist thrice except one,
    get the element that occur only once.

    ^ : is logically used when we want to use the logic
        if n not in once, then include n in once.
    & : is logically used to mask that is to use another
        binary to mask the data.
    ~ : is used to inverse the bits of the number.

    once = (once ^ num) & (~twice) : adds num to once only if num is not in 
        once and not in twice.
    twice = (twice ^ num) & (~once) : add num to twice only if num is not in 
        twice and not in once.
    """

    once = 0
    twice = 0
    for num in nums:
        once = (once ^ num) & (~twice)
        twice = (twice ^ num) & (~once)
    return once



if __name__ == "__main__":
    nums = [4,1,2,1,2]
    print(check_single_number(nums))

    nums = [1,2,3,4,2,3,2,3,4]
    print(check_single_number_2(nums))