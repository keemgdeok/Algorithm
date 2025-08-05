def solution(record):
    ans = []
    res = []
    user = {}
    for rec in record:
        msg = rec.split(" ")
        if msg[0] == "Enter": 
            user[msg[1]] = msg[2]
            res.append((msg[1],"님이 들어왔습니다."))
        elif msg[0] == "Change":
            user[msg[1]]=msg[2]
        else:
            res.append((msg[1],"님이 나갔습니다."))
    
    for uid, name in res:
        ans.append(f"{user[uid]}{name}")
    
    return ans