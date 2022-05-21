# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    ans = 0

    if A%K==0: ans += 1
    
    ans += B//K - A//K

    return ans
Analysis summary
