def solution(genres, plays):
    answer = []
    album = dict()
    
    # 딕셔너리에 입력 추가
    for i in range(len(plays)):
        if genres[i] not in album.keys():
            album.setdefault(genres[i], [[i, plays[i]]])
        else:
            album[genres[i]].append([i,plays[i]])
    
    # 곡 정렬
    for key, item in album.items():
        album[key] = sorted(album[key], key=lambda x: -x[1])
    
    # 전체 정렬
    sorted_album = dict(sorted(album.items(), key=lambda item: -sum(inner[1] for inner in item[1])))
    
    # 2개씩만
    for key, item in sorted_album.items():
        for i in range(min(2, len(item))):
            answer.append(item[i][0])
    
    return answer