# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    ans = 0
    left = [0 for _ in range(len(A))]
    right = [0 for _ in range(len(A))]
    
    for i in range(1, len(A)): left[i] = max(0, left[i-1] + A[i])
    for i in range(len(A)-2, 1, -1): right[i] = max(0, right[i+1]+A[i])

    for i in range(1, len(A)-1):
        ans = max(ans, left[i-1]+right[i+1])

    return ans
