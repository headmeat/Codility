# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    ans = []
    dp = [[0 for _ in range(4)] for _ in range(len(S)+1)]
    dic = {"A":0, "C":1, "G":2, "T":3}

    dp[1][dic[S[0]]] += 1

    for i in range(1, len(S)):
        for j in range(4):
            bias = 0
            if j==dic[S[i]]: bias = 1

            dp[i+1][j] += dp[i][j] + bias

    for i in range(len(P)):
        front, rear = P[i], Q[i]+1
        
        for j in range(4):
            if dp[rear][j]>dp[front][j]: 
                ans.append(j+1)
                break

    return ans
