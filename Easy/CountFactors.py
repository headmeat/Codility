# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    ans = 2 if N>1 else 1

    for i in range(2, int(N**0.5)+1):
        if N==i**2: ans += 1
        elif N % i == 0: ans += 2

    return ans
