# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    east = ans = 0

    for i in range(len(A)):
        if A[i]==0: east += 1
        else: ans += east

        if ans>10**9: return -1

    return ans
