'''
Set: Find Pairs ( ** Interview Question)
You are given two lists of integers, arr1 and arr2, and a target integer value, target. Your task is to find all pairs of numbers (one from arr1 and one from arr2) whose sum equals target.

Write a function called find_pairs that takes in three arguments: arr1, arr2, and target, and returns a list of all such pairs.  Assume that each array does not contain duplicate values.

Input

Your function should take in the following inputs:

arr1: a list of integers

arr2: a list of integers

target: an integer


Output

Your function should return a list of tuples, where each tuple contains two integers from arr1 and arr2 that add up to target.



Example 1:

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
target = 9

pairs = find_pairs(arr1, arr2, target)
print (pairs)
# Expected output: [(3, 6)]
# Explanation: There's only one pair that adds up to 9: 3 from arr1 and 6 from arr2.


Example 2:

arr1 = [0, 1, 2]
arr2 = [7, 8, 9]
target = 10

pairs = find_pairs(arr1, arr2, target)
print (pairs)
# Expected output: [(1, 9), (2, 8)]
# Explanation: The pairs that add up to 10 are (1, 9) and (2, 8).
'''


def find_pairs(arr1, arr2, target):
    set1 = set(arr1)
    pairs = []
    for num in arr2:
        complement = target - num
        if complement in set1:
            pairs.append((complement, num))
    return pairs




arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""

