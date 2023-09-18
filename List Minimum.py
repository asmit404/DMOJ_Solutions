"""
Title       : List Minimum
Link        : https://dmoj.ca/problem/bf1
Author      : Asmit Singh
Solved On   : 18 Sept 2023
Solved Using    : Python3
"""

pool = sorted([int(input()) for _ in range(int(input()))])
print(*pool, sep='\n')

# Also works for https://dmoj.ca/problem/bf1hard
# Time Complexity  : O(nlogn)
# Space Complexity : O(n)