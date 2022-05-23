# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    profit = 0
    least = A[0] if A else -1
    if least==-1: return 0

    for i in range(1, len(A)):
        profit = max(A[i] - least, profit)
        least = min(A[i], least)

    return profit
