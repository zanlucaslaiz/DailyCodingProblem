"""
HARD

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""

def rec(nums, idx):
    if idx >= len(nums):
        return 0
    return max(nums[idx] + rec(nums, idx + 2), rec(nums, idx + 1))
 
def findMaxSum(arr, N):
    return rec(arr, 0)
 
if __name__ == "__main__":
    # Creating the array
    arr = [7, 2, 3, 9, 15, 8]
    N = len(arr)
 
    # Function call
    print(findMaxSum(arr, N))