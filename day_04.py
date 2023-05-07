"""
HARD

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.


"""
from typing import List


def firstMissingPositiveInteger(arr: List[int]) -> int:
    length = len(arr)
    for i in range(length):
        correctPos = arr[i] - 1
        while 1 <= arr[i] <= length and arr[i] != arr[correctPos]:
            arr[i], arr[correctPos] = arr[correctPos], arr[i]
            correctPos = arr[i] - 1

    for i in range(length):
        if i + 1 != arr[i]:
            return i + 1
    return length + 1


if __name__ == "__main__":
    print(firstMissingPositiveInteger([3, 4, 2, 1]))
    print(firstMissingPositiveInteger([3, 4, -1, 1]))
    print(firstMissingPositiveInteger([1, 2, 5]))
    print(firstMissingPositiveInteger([-1, -2]))