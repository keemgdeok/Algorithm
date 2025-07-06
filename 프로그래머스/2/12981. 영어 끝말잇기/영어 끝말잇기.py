def solution(n, words):
    loop=dict()
    last_word = words[0][-1]
    loop[words[0]]=1
    
    for i in range(1, len(words)):
        if words[i] in loop:
            loop[words[i]]+=1
        else:
            loop[words[i]]=1

        if loop[words[i]]==2 or last_word != words[i][0]:
            return [i%n+1, i//n+1]
        last_word = words[i][-1]
        
    return [0, 0]