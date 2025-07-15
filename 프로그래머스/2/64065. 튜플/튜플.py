def solution(s):
    ans = []
    s= s.replace('{', '')
    s= s.replace('}', '')
    
    digit=''
    res = []
    for i in list(''.join(s)):
        if i != ',':
            digit+=i
        else:
            res.append(int(digit))
            digit=''
    res.append(int(digit))
    # print(res)
    
    count = dict()
    for r in res:
        if r not in count:
            count.setdefault(r, 1)
        else:
            count[r]+=1
            
    count = sorted(count.items(), key=lambda x: -x[1])
    
    for key, value in count:
        ans.append(key)
    
    
    return ans
