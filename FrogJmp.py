# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    Y -= X
    
    if Y%D: return Y//D + 1
    else: return Y//D
