# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    stack = []
    dic = {"{":"}", "(":")", "[":"]"}

    for i in range(len(S)):
        if S[i] in dic.keys(): stack.append(S[i])
        elif stack:
            if S[i] != dic[stack.pop()]: return 0
        else: return 0

    if stack: return 0
    else: return 1
