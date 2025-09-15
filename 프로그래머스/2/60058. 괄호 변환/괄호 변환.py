import sys
sys.setrecursionlimit(10**9)

def solution(p):
    return gaolho(p)

def gaolho(string):
    if not string:
        return ""
    
    # u, v
    u = ''; v = ''
    left = 0; right = 0
    for i in range(len(string)):
        if string[i]=='(': left+=1
        else: right+=1
        
        if left>0 and right>0 and left==right:
            u=string[:i+1]
            v=string[i+1:]
            break
            
    if checkcorrect(u):
        return u + gaolho(v)
    else:
        temp = '(' + gaolho(v) + ')'
        u_processed = fourfour(u)
        return temp + u_processed


def checkcorrect(string):
    check=[]
    for i in range(len(string)):
        if string[i]=="(":
            check.append(string[i])
        else:
            if check:
                check.pop()
            else:
                return False
    
    if not check:
        return True
    return False

def fourfour(u):
    result=''
    for s in u[1:-1]:
        if s=='(':
            result+=')'
        else:
            result+='('
        
    return result 

    
    
    