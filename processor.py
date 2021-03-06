class OperationError(Exception):
    pass


def sub_matrix(orig_matrix, i_exclude, j_exclude):
    matrix = []
    for i in range(len(orig_matrix)):
        if i != i_exclude:
            matrix.append(orig_matrix[i][:j_exclude] + orig_matrix[i][j_exclude + 1:])
    return matrix


def calc_determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    for j in range(len(matrix[0])):
        return sum([matrix[0][j] * calc_determinant(sub_matrix(matrix, 0, j)) * (-1)**j
                for j in range(len(matrix[0]))])


while True:
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
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

        if menu_opt == "5":
            (n_a, m_a) = map(int, input("Enter matrix size: ").split())
            print("Enter matrix:")
            A = []
            for _ in range(n_a):
                row = list(map(float, input().split()))
                if len(row) != m_a:
                    raise OperationError
                A.append(row)
            det = calc_determinant(A)
            print("The result is:")
            print(det)

        if menu_opt == "6":
            (n_a, m_a) = map(int, input("Enter matrix size: ").split())
            print("Enter matrix:")
            A = []
            for _ in range(n_a):
                row = list(map(float, input().split()))
                if len(row) != m_a:
                    raise OperationError
                A.append(row)
            C = [[0 for y in range(m_a)] for x in range(n_a)]
            for i in range(n_a):
                for j in range(m_a):
                    C[i][j] = calc_determinant(sub_matrix(A, i, j)) * (-1)**(i+j)
            C_transpose = [[0 for y in range(m_a)] for x in range(n_a)]
            for i in range(n_a):
                for j in range(m_a):
                    C_transpose[i][j] = C[j][i]
            det_A = calc_determinant(A)
            A_inv = []
            for i in range(n_a):
                A_inv.append([])
                for j in range(m_a):
                    A_inv[i].append((1 / det_A) * C_transpose[i][j])
            print("The result is:")
            for i in range(n_a):
                print(" ".join(list(map(str, A_inv[i]))))

    except OperationError:
        print("The operation cannot be performed.")

    print()
