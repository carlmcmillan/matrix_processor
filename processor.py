(n_a, m_a) = map(int, input().split())
A = []
for _ in range(n_a):
    row = list(map(int, input().split()))
    if len(row) != m_a:
        print("ERROR")
        exit(1)
    A.append(row)

c = int(input())

c_A = []
for i in range(n_a):
    c_A.append([])
    for j in range(m_a):
        c_A[i].append(c * A[i][j])

for i in range(n_a):
    print(" ".join(list(map(str, c_A[i]))))
