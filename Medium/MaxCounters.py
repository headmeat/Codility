# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    count = [0 for _ in range(N)]
    ground = 0
    mx = 0

    for i in range(len(A)):
        if A[i]>N: 
            ground = mx
            continue

        if count[A[i]-1]<ground:
            count[A[i]-1] = ground+1
        else:
            count[A[i]-1] += 1
        
        mx = max(mx, count[A[i]-1])

    for i in range(len(count)):
        if count[i]<ground: count[i] = ground

    return count
