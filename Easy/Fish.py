def solution(A, B):
    stack = []
    ans = 0

    for i in range(len(A)):
        if B[i]==1: 
            stack.append(A[i])
        else:
            while(stack):
                fish = stack.pop()
                if A[i]<fish:
                    stack.append(fish)
                    break

            if len(stack)==0: ans += 1

    return len(stack)+ans
