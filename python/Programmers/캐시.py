'''
그대로 구현
'''

def solution(cacheSize, cities):
    answer = 0
    cache = []
    # 캐시 사이즈가 0이면 결국 각각의 값을 조회하는데 항상 5의 시간이 걸림
    if cacheSize == 0:
        return len(cities) * 5
    
    for i in range(len(cities)):
        city = cities[i].upper()
        if city in cache:
            answer += 1
            idx = cache.index(city)
            cache.pop(idx)
            cache.append(city)
        else:
            answer += 5
            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(city)
            
    return answer