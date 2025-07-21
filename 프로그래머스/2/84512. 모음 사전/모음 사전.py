import sys
sys.setrecursionlimit(10**9)

cnt = 0
ans = 0
def solution(word):
    global ans
    dfs(word, "")
    
    return ans

def dfs(word, curr):
    global cnt, ans
    if word == curr:
        ans = cnt
        return True
    
    if len(curr) == 5:
        return False

    vowels = ["A", "E", "I", "O", "U"]
    for vow in vowels:
        cnt+=1
        if dfs(word, curr + vow):
            return True
        
    return False
        
    
    