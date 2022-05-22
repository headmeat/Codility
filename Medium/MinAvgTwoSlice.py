# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    minimum = (A[0]+A[1])/2
    idx = 0

    for i in range(2, len(A)):
        two = (A[i]+A[i-1])/2
        if two<minimum: 
            minimum = two
            idx = i-1
        three = (A[i]+A[i-1]+A[i-2])/3
        if three<minimum: 
            minimum = three
            idx = i-2

    return idx
