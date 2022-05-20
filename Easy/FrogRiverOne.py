# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    leaves = {}
    sm = 0
    leap = X*(X+1)//2

    for i in range(len(A)):
        if A[i]<=X:
            if A[i] not in leaves.keys():
                leaves[A[i]] = True
                sm += A[i]

            if sm == leap: return i

    return -1
