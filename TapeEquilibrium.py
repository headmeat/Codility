# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    noo = [0 for _ in range(len(A))]
    noo[0] = A[0]
    ans = 10**10

    for i in range(1, len(A)):
        noo[i] = noo[i-1] + A[i]

    for i in range(len(noo)-1):
        ans = min(ans, abs(noo[-1] - 2*noo[i]))

    return ans
