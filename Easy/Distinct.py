# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A.sort()
    ans = 0
    if len(A)>0: ans += 1

    for i in range(1, len(A)):
        if A[i] != A[i-1]: ans += 1

    return ans
