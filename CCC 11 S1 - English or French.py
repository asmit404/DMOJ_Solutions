"""
Title       : CCC '11 S1 - English or French?
Link        : https://dmoj.ca/problem/ccc11s1
Author      : Asmit Singh
Solved On   : 13 Sept 2023
Solved Using    : Python3
"""

def lang():
    n = int(input())
    flag = False

    pool = [input() for _ in range(n)]
    pool = " ".join(pool)

    tCount = pool.count("t") + pool.count("T")
    sCount = pool.count("s") + pool.count("S")

    if tCount > sCount:
        flag = True
    if sCount > tCount:
        flag = False
    if sCount == tCount:
        flag = False

    return "English" if flag else "French"

print(lang())
