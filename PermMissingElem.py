# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    visited = [0 for _ in range(len(A)+1)]

    for i in range(len(A)):
        visited[A[i]-1] = 1

    for i in range(len(visited)):
        if visited[i] == 0: return i+1
