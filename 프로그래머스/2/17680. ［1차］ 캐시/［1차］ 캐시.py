def solution(cacheSize, cities):
    ans = 0
    cache = []
    cities = [city.lower() for city in cities]
    cache.append(cities[0])
    ans+=5
    
    if cacheSize == 0:
        return len(cities)*5
    
    
    for i in range(1, len(cities)):
        if cities[i] in cache:
            cache.remove(cities[i])
            cache.append(cities[i])
            ans+=1    
        else:
            if len(cache) >= cacheSize:
                cache.pop(0)
            cache.append(cities[i])
            ans+=5  

    return ans