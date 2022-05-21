def solution(A):
    arr = [0 for _ in range(1000001)]

    for i in range(len(A)):
        if A[i]<1: continue

        arr[A[i]] = 1

    for i in range(1, len(arr)):
        if arr[i]==0: return i
