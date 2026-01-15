def solution(answers):
    ans = []
    n1 = [1, 2, 3, 4, 5]
    n2 = [2, 1, 2, 3, 2, 4, 2, 5]
    n3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    ans = [0,0,0]
    for i in range(len(answers)):
        if answers[i] == n1[i%len(n1)]:
            ans[0]+=1
        if answers[i] == n2[i%len(n2)]:
            ans[1]+=1
        if answers[i] == n3[i%len(n3)]:
            ans[2]+=1

    n = max(ans)
    res = []
    for i,a in enumerate(ans):
        if n == a:
            res.append(i+1) 
    
    return res