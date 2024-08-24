i=0
while True:
    L,P,V=map(int, input().split())
    if L==0 and P==0 and V==0: break
    i+=1
    
    n=V//P
    m=V%P

    if L<m: m=L
        

    print(f"Case {i}:",n*L+m)
