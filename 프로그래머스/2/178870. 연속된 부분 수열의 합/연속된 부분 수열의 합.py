def solution(seq, k):
    left = 0
    curr = 0
    min_len = float('inf')
    res = []
    
    
    for right in range(len(seq)):
        curr += seq[right]
        
        while curr > k and left <=right:
            curr -= seq[left]
            left+=1
            
        if curr == k:
            length = right - left + 1
            if length < min_len:
                min_len = length
                res = [left, right]
            elif length == min_len and left < res[0]:
                res = [left, right]
    return res
