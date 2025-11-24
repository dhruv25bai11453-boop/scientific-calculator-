import cmath

def get_number(prompt):
    """
    Asks for a number (e.g., 4.5 or 3+4j). Also accepts 'm' for matrix mode.
    Keeps asking until correct.
    """
    while True:
        s = input(prompt).strip()
        if s.lower() == 'm':
            return 'm'
        try:
            return complex(s)
        except ValueError:
            print("Please enter a valid number (like 5 or 3+4j), or 'm' for matrix mode.")

def get_matrix(name):
    """
    Prompts user to enter a matrix row by row as a list of lists.
    Returns a list of lists (rows of complex numbers).
    """
    print(f"\n-- Enter Matrix {name} --")
    rows = int(input(f"Rows for Matrix {name}: "))
    cols = int(input(f"Columns for Matrix {name}: "))
    matrix = []
    for i in range(rows):
        while True:
            row_input = input(f"Row {i+1} (e.g. 1 2 3): ")
            try:
                row = [complex(x) for x in row_input.strip().split()]
                if len(row) == cols:
                    matrix.append(row)
                    break
                else:
                    print(f"That row needs exactly {cols} items. Please try again.")
            except ValueError:
                print("Numbers only, separated by spaces (e.g. 1 2+3j 5).")
    return matrix

def matrix_shape(matrix):
    """
    Returns shape (rows, cols) for a list-of-lists matrix.
    """
    if not matrix:
        return (0, 0)
    return (len(matrix), len(matrix[0]))

def add_matrices(mat_a, mat_b):
    """
    Adds two matrices of same shape.
    """
    rows, cols = matrix_shape(mat_a)
    return [[mat_a[i][j] + mat_b[i][j] for j in range(cols)] for i in range(rows)]

def multiply_matrices(mat_a, mat_b):
    """
    Multiplies two matrices where A_cols == B_rows.
    """
    a_rows, a_cols = matrix_shape(mat_a)
    b_rows, b_cols = matrix_shape(mat_b)
    # Matrix multiplication
    result = []
    for i in range(a_rows):
        row = []
        for j in range(b_cols):
            cell = sum(mat_a[i][k] * mat_b[k][j] for k in range(a_cols))
            row.append(cell)
        result.append(row)
    return result

# Friendly calculator intro
print("\nWelcome to the Calculator!\n")
print("You can use real/complex numbers (e.g., 4, 3+2j), or matrices.")
print("Operators: +, -, *, /, %, sin, cos, tan, MAT_ADD, MAT_MUL")
print("* Type 'm' instead of a number to enter Matrix mode *\n")

a = get_number("Enter your first number (or 'm' for Matrix): ")
if a == 'm':    
    mat_a = get_matrix('A')
    a_is_matrix = True
else:
    a_is_matrix = False
b = get_number("Enter your second number (or 'm' for Matrix): ")
if b == 'm':    
    mat_b = get_matrix('B')
    b_is_matrix = True
else:
    b_is_matrix = False
b_is_matrix = False
# Determine operation
if a_is_matrix and b_is_matrix:
    print("\nMatrix Operations Available: MAT_ADD, MAT_MUL")
    op = input("Enter operation (MAT_ADD or MAT_MUL): ").strip().upper()
    if op == 'MAT_ADD':
        if matrix_shape(mat_a) != matrix_shape(mat_b):
            print("Error: Matrices must have the same shape for addition.")
        else:
            result = add_matrices(mat_a, mat_b)
            print("\nResultant Matrix:")
            for row in result:
                print(" ".join(str(x) for x in row))
    elif op == 'MAT_MUL':
        if matrix_shape(mat_a)[1] != matrix_shape(mat_b)[0]:
            print("Error: A's columns must equal B's rows for multiplication.")
        else:
            result = multiply_matrices(mat_a, mat_b)
            print("\nResultant Matrix:")
            for row in result:
                print(" ".join(str(x) for x in row))
    else:
        print("Invalid matrix operation.")
elif not a_is_matrix and not b_is_matrix:
    print("\nNumeric Operations Available: +, -, *, /, %, sin, cos, tan")
    op = input("Enter operation (+, -, *, /, %, sin, cos, tan): ").strip()
    try:
        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            result = a / b
        elif op == '%':
            result = a % b
        elif op == 'sin':
            result = cmath.sin(a)
        elif op == 'cos':
            result = cmath.cos(a)
        elif op == 'tan':
            result = cmath.tan(a)
        else:
            print("Invalid operation.")
            exit()
        print(f"\nResult: {result}")
    except Exception as e:
        print(f"Error during calculation: {e}")
# ...existing code...