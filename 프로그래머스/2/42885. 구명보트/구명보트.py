def solution(people, limit):
    answer = 0
    people.sort()
    
    left=0
    right=len(people)-1
    
    while left<=right:
        if len(people)==0:
            break
        
        if people[left] + people[right] <= limit:
            right-=1
            left+=1
        else:
            right-=1
            
        answer+=1
    
    
    return answer