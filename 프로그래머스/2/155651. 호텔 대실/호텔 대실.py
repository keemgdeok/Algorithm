def solution(book_time):
    ans = 0
    rooms=[]
    book_time.sort()

    for start, end in book_time:
        sh, sm = map(int, start.split(":"))
        eh, em = map(int, end.split(":"))
        stime = sh*60 + sm
        etime = eh*60 + em
        
        flag=0
        for i in range(len(rooms)):
            if rooms[i]+10 <= stime:
                rooms[i]=etime
                flag=1
                break
                
        if flag==0:
            rooms.append(etime)
            
    return len(rooms)