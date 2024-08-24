import sys
input=sys.stdin.readline

N,M=map(int, input().split())
board=[]
for _ in range(N):
    board.append(input())


ans=[]
for i in range(N-7):
    for j in range(M-7):
        cnt1=0; cnt2=0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b)%2==0:
                    if board[a][b]!='W':
                        cnt2+=1
                    if board[a][b]!='B':
                        cnt1+=1
                else:
                    if board[a][b]!='W':
                        cnt1+=1
                    if board[a][b]!="B":
                        cnt2+=1
        ans.append(min(cnt1, cnt2))

print(min(ans))