from collections import deque

def solution(begin, target, words):
    dq=deque()
    visited=[0]*(len(words))
    
    dq.append((begin, 1))
    while True:
        if not dq:
            print("EXIT")
            return 0
        
        word, n = dq.popleft()
        for i in range(len(words)):
            if visited[i]==0 and checkWord(word, words[i]):
                dq.append((words[i], n+1))
                visited[i]=1
                        
        print("word", word)
        if word == target:
            for i in range(len(words)):
                if target == words[i]:
                    break
            return n-1
    

def checkWord(word1, word2):
    res =  sum(1 for a, b in zip(word1, word2) if a!=b)
    
    return res == 1
