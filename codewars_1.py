def count_by(x, n):
    list_ = []
    k = (n * 100)+150
    p = range(x, k)
    for i in p:
        if i % x == 0:
            list_.append(i)
    return list_[:n]






b = count_by(100,5)
print(b)
