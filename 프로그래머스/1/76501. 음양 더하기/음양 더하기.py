def solution(absolutes, signs):
    ans=0
    for ab, sign in zip(absolutes, signs):
        if sign==True:
            ans+=ab
        else:
            ans-=ab
    return ans
        