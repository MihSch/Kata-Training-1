def count_by(x, n):
    list_ = []
    k = (n * 100)+150
    for i in range(x, k):
        if i % x == 0:
            list_.append(i)
    return list_[:n]






print(count_by(100,5))
