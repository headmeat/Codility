import heapq

def solution(A):
    circle = []
    q = []
    ans = 0

    for i in range(len(A)):
        circle.append((i-A[i], i+A[i]))

    circle.sort(key=lambda x: x[0])

    for i in range(len(circle)):
        left, right = circle[i]

        while(q):
            tmp = heapq.heappop(q)

            if tmp>=left:
                heapq.heappush(q, tmp)
                break

        ans += len(q)
        if ans>10000000: return -1
        heapq.heappush(q, right)

    return ans
