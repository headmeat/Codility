# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(K, A):
    sm = ans = 0

    for i in range(len(A)):
        sm += A[i]

        if sm>=K:
            ans += 1
            sm = 0

    return ans
