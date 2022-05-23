# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    lines = []

    for i in range(len(A)):
        lines.append((A[i], B[i]))

    lines.sort(key = lambda x: (x[1], x[0]))
    ans = 1 if lines else 0
    prev = lines[0][1] if lines else 0

    for i in range(1, len(lines)):
        if prev<lines[i][0]: 
            ans += 1
            prev = lines[i][1]

    return ans
