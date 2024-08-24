N=int(input())

count=0
while N>=0:
    if N%5==0:
        count += (N//5)
        print(count)
        break
    N-=3
    count+=1
else:
    print(-1)

# 3보다 5가 큰값이므로 
# 5의 배수가 될때까지 설탕의 무개에서 3씩 뺴가는 방식이다.
# 그래야 봉지의 최소 개수를 구할 수 있다.

