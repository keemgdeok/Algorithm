import itertools

def solution(orders, course):
    ans = []
    menu = {}
    for order in orders:
        order
        for c in course:
            if len(order) >= c:
                comb = list(itertools.combinations(order, c))

                for res in comb:
                    m = "".join(sorted(res))
                    if m not in menu:
                        menu[m]=1
                    else:
                        menu[m]+=1
                    
    comb_menu = {key: value for key, value in menu.items() if value != 1}
    for course_size in course:
        cnt=0
        for key, value in comb_menu.items():
            if course_size == len(key):
                cnt=max(cnt, value)
        for key, value in comb_menu.items():
            if course_size == len(key) and cnt==value:
                ans.append(key)
                    
    return sorted(ans)