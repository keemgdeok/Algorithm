def solution(skill, skill_trees):
    ans = 0
    for tree in skill_trees:
        filtered = ""
        for t in tree:
            if t in skill:
                filtered+=t
                
        if skill.startswith(filtered):
            ans+=1
                
    return ans