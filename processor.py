class OperationError(Exception):
    pass


while True:
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("0. Exit")
    menu_opt = input("Your choice: ")

    if menu_opt == "0":
        break

    try:
        if menu_opt == "1":
            (n_a, m_a) = map(int, input("Enter size of first matrix: ").split())
            print("Enter first matrix:")
            A = []
            for _ in range(n_a):
                row = list(map(float, input().split()))
                if len(row) != m_a:
                    raise OperationError
                A.append(row)
            (n_b, m_b) = map(int, input("Enter size of second matrix: ").split())
            print("Enter second matrix:")
            B = []
            for _ in range(n_b):
                row = list(map(float, input().split()))
                if len(row) != m_b:
                    raise OperationError
                B.append(row)
            if n_a != n_b or m_a != m_b:
                raise OperationError
            A_B = []
            for i in range(n_a):
                A_B.append([])
                for j in range(m_a):
                    A_B[i].append(A[i][j] + B[i][j])
            print("The result is:")
            for i in range(n_a):
                print(" ".join(list(map(str, A_B[i]))))

        if menu_opt == "2":
            (n_a, m_a) = map(int, input("Enter size of matrix: ").split())
            print("Enter matrix:")
            A = []
            for _ in range(n_a):
                row = list(map(float, input().split()))
                if len(row) != m_a:
                    raise OperationError
                A.append(row)
            c = float(input("Enter constant: "))
            c_A = []
            for i in range(n_a):
                c_A.append([])
                for j in range(m_a):
                    c_A[i].append(c * A[i][j])
            print("The result is:")
            for i in range(n_a):
                print(" ".join(list(map(str, c_A[i]))))

        if menu_opt == "3":
            (n_a, m_a) = map(int, input("Enter size of first matrix: ").split())
            print("Enter first matrix:")
            A = []
            for _ in range(n_a):
                row = list(map(float, input().split()))
                if len(row) != m_a:
                    raise OperationError
                A.append(row)
            (n_b, m_b) = map(int, input("Enter size of second matrix: ").split())
            print("Enter second matrix:")
            B = []
            for _ in range(n_b):
                row = list(map(float, input().split()))
                if len(row) != m_b:
                    raise OperationError
                B.append(row)
            if m_a != n_b:
                raise OperationError
            A_B = [[0 for y in range(m_b)] for x in range(n_a)]
            for a_i in range(n_a):
                for b_j in range(m_b):
                    val = 0
                    for a_j in range(m_a):
                        val += A[a_i][a_j] * B[a_j][b_j]
                    A_B[a_i][b_j] = val
            print("The result is:")
            for i in range(n_a):
                print(" ".join(list(map(str, A_B[i]))))

        if menu_opt == "4":
            print()
            print("1. Main diagonal")
            print("2. Side diagonal")
            print("3. Vertical line")
            print("4. Horizontal line")
            transpose_opt = input()
            (n_a, m_a) = map(int, input("Enter size of first matrix: ").split())
            print("Enter matrix:")
            A = []
            for _ in range(n_a):
                row = list(map(float, input().split()))
                if len(row) != m_a:
                    raise OperationError
                A.append(row)
            R = [[0 for y in range(m_a)] for x in range(n_a)]
            if transpose_opt == "1":
                for i in range(n_a):
                    for j in range(m_a):
                        R[i][j] = A[j][i]
            if transpose_opt == "2":
                for i in range(n_a):
                    for j in range(m_a):
                        R[i][j] = A[m_a - j - 1][n_a - i - 1]
            if transpose_opt == "3":
                for i in range(n_a):
                    for j in range(m_a):
                        R[i][j] = A[i][m_a - j - 1]
            if transpose_opt == "4":
                for i in range(n_a):
                    for j in range(m_a):
                        R[i][j] = A[n_a - i - 1][j]
            print("The result is:")
            for i in range(n_a):
                print(" ".join(list(map(str, R[i]))))

    except OperationError:
        print("The operation cannot be performed.")

    print()
