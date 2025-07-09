def solution(want, number, discount):
    ans = 0
    
    for i in range(len(discount)-9):
        n = number[:]

        for j in range(i, i+10):
            if discount[j] in want:
                ind = want.index(discount[j])
                n[ind]-=1
                
            for k in range(len(number)):
                if n[k] > 0:
                    break
                
                if k == len(number)-1:
                    ans+=1
            
        
    return ans