import math

def solution(m, musicinfos):
    ans = []
    m = codeMapping(m)
    for index, info in enumerate(musicinfos):
        start, end, song, sound = info.split(",")
        
        # 코드 변환
        sound = codeMapping(sound)
        
        # 재생 시간 계산
        hstart, mstart = map(int,start.split(":"))
        hend, mend = map(int,end.split(":"))
        if hend==0 and mend==0:   
            if hstart != 0 or mstart != 0: # 00:00~00:00 케이스 제외
                hend = 24
        playing = (hend-hstart)*60 + (mend-mstart)
        
        # 재생 코드 계산
        play=''
        play = sound * (playing//len(sound)) + sound[:playing%len(sound)]
        
        if m in play:
            ans.append((playing, index, song))

    
    if not ans:
        return "(None)"

    return sorted(ans, key=lambda x: (-x[0], x[1]))[0][-1]
    
    
def codeMapping(code):
    # 5개 mapping
    # C#:U , D#:V , F#:X , G#:Y , A#:Z 
    mapping = {
        'C#': 'U',
        'D#': 'V',
        'F#': 'X',
        'G#': 'Y',
        'A#': 'Z',
        'B#': "C",
        'E#': "F"
    }
    
    replaced = code
    for old, new in mapping.items():
        replaced = replaced.replace(old, new)
    
    return replaced
    
    
    
    