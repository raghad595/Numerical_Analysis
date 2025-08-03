import numpy as np
def display_matrix(mat, title="Matrix"):
    formatted = '\n'.join(['\t'.join([f"{val:.2f}" for val in row]) for row in mat])
    return f"{title}:\n{formatted}"

def det(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        # base case for 2x2 matrix
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    # recursive case for larger matrices
    detA = 0
    for c in range(n):
        minor = [row[:c] + row[c+1:] for row in matrix[1:]]  # exclude first row & column c
        detA += ((-1)**c) * matrix[0][c] * det(minor)
    return detA

def zeros(n):
    return [[0.0 for _ in range(n)] for _ in range(n)]

def identity(n):
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

def copy_matrix(mat):
    return [row[:] for row in mat]

def dot_product(a, b):
    return sum(x * y for x, y in zip(a, b))

def gauss_elimination(matrix):
    logs = []  # Initialize logs to store steps
    n = len(matrix)
    matrix = copy_matrix(matrix)  # Make a copy of the matrix to avoid modifying the original
    logs.append(display_matrix(matrix, "Initial Matrix"))  # Log the initial matrix

    # Forward elimination
    for i in range(n):
        pivot = matrix[i][i]
        if pivot == 0:
            logs.append(f"Zero pivot at row {i}, skipping...")
            continue
        matrix[i] = [x / pivot for x in matrix[i]]
        logs.append(display_matrix(matrix, f"After normalizing row {i + 1}"))

        for j in range(i + 1, n):
            factor = matrix[j][i]
            matrix[j] = [a - factor * b for a, b in zip(matrix[j], matrix[i])]
            logs.append(display_matrix(matrix, f"After eliminating row {j + 1}"))

    # Back substitution
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = matrix[i][-1] - sum(matrix[i][j] * x[j] for j in range(i + 1, n))
        logs.append(display_matrix(matrix, f"Back substitution step {n - i}"))

    return x, logs

def gauss_jordan_elimination(matrix):
    logs = []
    n = len(matrix)
    matrix = copy_matrix(matrix)
    logs.append(display_matrix(matrix, "Initial Matrix"))

    for i in range(n):
        pivot = matrix[i][i]
        if pivot == 0:
            logs.append(f"Zero pivot at row {i}, skipping...")
            continue
        matrix[i] = [x / pivot for x in matrix[i]]
        for j in range(n):
            if i != j:
                factor = matrix[j][i]
                matrix[j] = [a - factor * b for a, b in zip(matrix[j], matrix[i])]
        logs.append(display_matrix(matrix, f"After step {i + 1}"))

    x = [row[-1] for row in matrix]
    return x, logs

def gauss_elimination_partial_pivoting(matrix):
    logs = []
    n = len(matrix)
    matrix = copy_matrix(matrix)
    logs.append(display_matrix(matrix, "Initial Matrix"))

    for i in range(n):
        max_row = max(range(i, n), key=lambda r: abs(matrix[r][i]))
        if i != max_row:
            matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
            logs.append(display_matrix(matrix, f"After row swap {i + 1} (partial pivoting)"))

        pivot = matrix[i][i]
        if pivot == 0:
            logs.append(f"Zero pivot at row {i}, skipping...")
            continue
        matrix[i] = [x / pivot for x in matrix[i]]
        for j in range(i + 1, n):
            factor = matrix[j][i]
            matrix[j] = [a - factor * b for a, b in zip(matrix[j], matrix[i])]
        logs.append(display_matrix(matrix, f"After elimination step {i + 1}"))

    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = matrix[i][-1] - dot_product(matrix[i][i+1:n], x[i+1:n])
    return x, logs

def gauss_jordan_partial_pivoting(matrix):
    logs = []
    n = len(matrix)
    matrix = copy_matrix(matrix)
    logs.append(display_matrix(matrix, "Initial Matrix"))

    for i in range(n):
        max_row = max(range(i, n), key=lambda r: abs(matrix[r][i]))
        if i != max_row:
            matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
            logs.append(display_matrix(matrix, f"After row swap {i + 1} (partial pivoting)"))

        pivot = matrix[i][i]
        if pivot == 0:
            logs.append(f"Zero pivot at row {i}, skipping...")
            continue

        matrix[i] = [x / pivot for x in matrix[i]]
        for j in range(n):
            if i != j:
                factor = matrix[j][i]
                matrix[j] = [a - factor * b for a, b in zip(matrix[j], matrix[i])]
        logs.append(display_matrix(matrix, f"After step {i + 1}"))

    x = [row[-1] for row in matrix]
    return x, logs

def lu_decomposition(matrix_data):
    logs = []
    A = [row[:-1] for row in matrix_data]  # Coefficients
    b = [row[-1] for row in matrix_data]   # Constants
    n = len(A)
    L = zeros(n)
    U = zeros(n)

    for i in range(n):
        for k in range(i, n):
            sum_ = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = A[i][k] - sum_
        L[i][i] = 1
        for k in range(i + 1, n):
            sum_ = sum(L[k][j] * U[j][i] for j in range(i))
            L[k][i] = (A[k][i] - sum_) / U[i][i]

        logs.append(display_matrix(L, f"L after step {i + 1}"))
        logs.append(display_matrix(U, f"U after step {i + 1}"))

    # Forward substitution (solve LC = b)
    c = [0.0] * n
    for i in range(n):
        c[i] = b[i] - sum(L[i][j] * c[j] for j in range(i))

    logs.append("LC = b")
    logs.append(display_matrix(L, "Lower Matrix L") + " * " + display_matrix([[val] for val in c], "C") + " = " + display_matrix([[val] for val in b], "B"))

    # Back substitution (solve Ux = c)
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (c[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))) / U[i][i]

    logs.append("Ux = c")
    logs.append(display_matrix(U, "Upper Matrix U") + " * " + display_matrix([[val] for val in x], "X") + " = " + display_matrix([[val] for val in c], "C"))

    return L, U, x, logs

def lu_decomposition_partial_pivoting(matrix_data):
    logs = []
    A = [row[:-1] for row in matrix_data]  # Coefficients
    b = [row[-1] for row in matrix_data]   # Constants
    n = len(A)
    
    L = identity(n)
    U = zeros(n)
    P = identity(n)
    for i in range(n):
        max_row = max(range(i, n), key=lambda r: abs(A[r][i]))
        if i != max_row:
            A[i], A[max_row] = A[max_row], A[i]
            P[i], P[max_row] = P[max_row], P[i]
            L[i][:i], L[max_row][:i] = L[max_row][:i], L[i][:i]
            logs.append(display_matrix(A, f"A after partial pivoting at step {i+1}"))
        for j in range(i, n):
            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))
        for j in range(i+1, n):
            L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]
        logs.append(display_matrix(L, f"L after step {i+1}"))
        logs.append(display_matrix(U, f"U after step {i+1}"))
    # Forward substitution (solve LC = b)
    c = [0.0] * n
    for i in range(n):
        c[i] = b[i] - sum(L[i][j] * c[j] for j in range(i))

    logs.append("LC = b")
    logs.append(display_matrix(L, "Lower Matrix L") + " * " + display_matrix([[val] for val in c], "C") + " = " + display_matrix([[val] for val in b], "B"))

    # Back substitution (solve Ux = c)
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (c[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))) / U[i][i]

    logs.append("Ux = c")
    logs.append(display_matrix(U, "Upper Matrix U") + " * " + display_matrix([[val] for val in x], "X") + " = " + display_matrix([[val] for val in c], "C"))
    return L, U, P, x, logs

def cramer(matrix_data):
    logs = []
    try:
        n = len(matrix_data)
        A = [row[:-1] for row in matrix_data]  # Coefficients
        B = [row[-1] for row in matrix_data]   # Constants

        det_A = det(A)
        if det_A == 0:
            logs.append("The system has no unique solution (det(A) = 0).")
            return None, logs

        solution = []
        for i in range(n):
            modified_matrix = [row[:] for row in A]  # Deep copy
            for j in range(n):
                modified_matrix[j][i] = B[j]  # Replace column i with constants
            det_modified = det(modified_matrix)
            solution.append(det_modified / det_A)
            logs.append(display_matrix(modified_matrix, f"Matrix with column {i + 1} replaced"))

        return solution, logs

    except Exception as e:
        logs.append(f"Error: {str(e)}")
        return None, logs
