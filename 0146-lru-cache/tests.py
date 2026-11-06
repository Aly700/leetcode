def run(solution):
    cache = solution.LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4

    single = solution.LRUCache(1)
    single.put(2, 1)
    assert single.get(2) == 1
    single.put(3, 2)
    assert single.get(2) == -1
    assert single.get(3) == 2
    single.put(3, 5)
    assert single.get(3) == 5
