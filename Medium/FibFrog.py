from sys import stdin
input = stdin.readline

def solution(A):
    A += [1]
    fibo = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025]
    frog = [0 for _ in range(len(A))]

    for i in range(len(A)):
        if A[i]==1:
            for j in range(len(fibo)):
                if i-fibo[j]<-1: continue
                if i-fibo[j]==-1: frog[i] = 1
                elif 0<=i-fibo[j]<len(frog) and frog[i-fibo[j]]:
                    if frog[i]: frog[i] = min(frog[i], frog[i-fibo[j]]+1)
                    else: frog[i] = frog[i-fibo[j]]+1

    if frog[-1]: return frog[-1]
    else: return -1
