# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    end = res = 0

    for i in range(len(A)):
        end = max(0, end+A[i])
        res = max(res, end)

    if (res==0 and 0 in A) or res>0: return res
    else: return max(A)
