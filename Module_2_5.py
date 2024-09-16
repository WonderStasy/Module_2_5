def get_matrix(n, m, value):
    a = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            a[i][j] = value
    return a
a = get_matrix(2, 2, 10)
b = get_matrix(3, 5, 42)
c = get_matrix(4, 2, 13)
print(a)
print(b)
print(c)