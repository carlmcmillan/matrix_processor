(n_a, m_a) = map(int, input().split())
A = []
for _ in range(n_a):
    row = list(map(int, input().split()))
    if len(row) != m_a:
        print("ERROR")
        exit(1)
    A.append(row)

(n_b, m_b) = map(int, input().split())
B = []
for _ in range(n_b):
    row = list(map(int, input().split()))
    if len(row) != m_b:
        print("ERROR")
        exit(1)
    B.append(row)

if n_a != n_b or m_a != m_b:
    print("ERROR")
    exit(1)

A_B = []
for i in range(n_a):
    A_B.append([])
    for j in range(m_a):
        A_B[i].append(A[i][j] + B[i][j])

for i in range(n_a):
    print(" ".join(list(map(str, A_B[i]))))
