def solution(participant, completion):
    from collections import Counter

    p = Counter(participant)
    c = Counter(completion)
    remainder = p - c
    
    return "".join(list(remainder))
