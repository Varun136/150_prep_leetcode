""" 
Given an array of integers citations where citations[i] is the number of citations a researcher 
received for their ith paper, return the researcher's h-index.
According to the definition of h-index on Wikipedia: The h-index is defined as the maximum 
value of h such that the given researcher has published at least h papers that have each been cited at least h times.
"""


def h_index(citations: int) -> int:
    # brute force approach

    n = len(citations)
    h_index = 0

    for i in range(1,n+1):
        count = 0
        for j in citations:
            if j >= i:
                count += 1
        if count >= i:
            h_index = i
        else:
            break
    return h_index


if __name__ == "__main__":
    nums = [3,0,6,1,5]
    print(h_index(nums))