# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    a, b = 1, N

    for i in range(2, int(N**0.5)+1):
        if N%i == 0: 
            a = i
            b = N//i

    return 2 * (a + b)
