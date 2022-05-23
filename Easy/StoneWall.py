# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    stack = [H[0]]
    ans = 1

    for i in range(1, len(H)):
        while(stack):
            if stack[-1]>H[i]: stack.pop()
            else: break
            
        if stack:
            if stack[-1]<H[i]: ans += 1
        else:
            ans += 1

        stack.append(H[i])

    return ans
