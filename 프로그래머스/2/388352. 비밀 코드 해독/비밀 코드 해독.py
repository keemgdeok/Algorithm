import itertools

def solution(n, q, ans):
    answer = 0
    
    passwd = list(range(1, n+1))
    comb_passwd = list(itertools.combinations(passwd, 5))
    
    # 일치 개수 구하기
    for pwd in comb_passwd:
        flag = 0
        for i in range(len(q)):
            if checkpwd(q[i], pwd) == ans[i]:
                flag+=1
        if flag == len(q):
            answer+=1
            
    return answer

def checkpwd(qq, checklist):
    count = 0
    for i in range(5):
        if qq[i] in checklist:
            count+=1
            
    return count
    