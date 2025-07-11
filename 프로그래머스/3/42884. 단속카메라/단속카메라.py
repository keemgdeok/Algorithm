def solution(routes):
    ans = 0
    n = len(routes)

    routes.sort(key=lambda x: x[1])
    camera=routes[0][1]
    print(routes)
    for i in range(1, n):
        if camera < routes[i][0]:
            camera = routes[i][1]
            ans+=1
            print(camera)
        

    return ans + 1