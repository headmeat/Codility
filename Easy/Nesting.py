# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    stack = []

    for i in range(len(S)):
        if S[i]=="(": stack.append(S[i])
        elif stack: stack.pop()
        else: return 0

    if stack: return 0
    else: return 1
