import numpy as np
# Function to display the matrix menu
def matrix_menu():
    print("---------------------------- MATRIX MENU -----------------------------------")
    print("Matrix Operations Menu:")
    print("1. Matrix Addition")
    print("2. Matrix Subtraction")
    print("3. Matrix Multiplication")
    print("4. Matrix Transpose")
    print("5. Matrix Determinant")
    print("6. Matrix Inverse")
    print("7. Matrix Adjoint")
    print("8. Exit (go back to main menu)")
    print("0. CLOSE THE PROGRAM")
    print("---------------------------------------------------------------")

# Function to take matrix input from the user
def input_matrix():
    while True:
        try:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            if rows <= 0 or cols <= 0:
                raise ValueError("The number of rows and columns must be positive integers.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter valid positive integers.")

    matrix = []
    print(f"Enter the elements of {rows}x{cols} matrix (row-wise):")

    for i in range(rows):
        while True:
            try:
                row = list(map(float, input(f"Enter row {i+1} (separate elements with spaces): ").split()))
                if len(row) != cols:
                    raise ValueError(f"Row {i+1} must have exactly {cols} elements.")
                matrix.append(row)
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")
    
    return np.array(matrix)

# Matrix operations functions
def add_matrices(mat1, mat2):
    return np.add(mat1, mat2)

def subtract_matrices(mat1, mat2):
    return np.subtract(mat1, mat2)

def multiply_matrices(mat1, mat2):
    return np.dot(mat1, mat2)

def transpose_matrix(mat):
    return np.transpose(mat)

def determinant_matrix(mat):
    return np.linalg.det(mat)

def inverse_matrix(mat):
    try:
        inv = np.linalg.inv(mat)
        return inv
    except np.linalg.LinAlgError:
        return None

def adjoint_matrix(mat):
    det = determinant_matrix(mat)
    if det == 0:
        print("The matrix is singular; no adjoint exists.")
        return None
    cofactors = np.linalg.inv(mat).T * det  # Adjoint = transpose of cofactor matrix
    return cofactors

# Main function to run the program
def run_Matrix():
    while True:
        matrix_menu()
        choice = input("Choose an operation (1-8): ")

        if choice == '1':  # Matrix Addition
            print("Matrix 1:")
            mat1 = input_matrix()
            print("Matrix 2:")
            mat2 = input_matrix()
            if mat1.shape == mat2.shape:
                print("Result of addition:")
                print(add_matrices(mat1, mat2))
            else:
                print("Matrices must have the same dimensions for addition.")

        elif choice == '2':  # Matrix Subtraction
            print("Matrix 1:")
            mat1 = input_matrix()
            print("Matrix 2:")
            mat2 = input_matrix()
            if mat1.shape == mat2.shape:
                print("Result of subtraction:")
                print(subtract_matrices(mat1, mat2))
            else:
                print("Matrices must have the same dimensions for subtraction.")

        elif choice == '3':  # Matrix Multiplication
            print("Matrix 1:")
            mat1 = input_matrix()
            print("Matrix 2:")
            mat2 = input_matrix()
            if mat1.shape[1] == mat2.shape[0]:
                print("Result of multiplication:")
                print(multiply_matrices(mat1, mat2))
            else:
                print("Number of columns of Matrix 1 must be equal to the number of rows of Matrix 2.")

        elif choice == '4':  # Matrix Transpose
            print("Matrix:")
            mat = input_matrix()
            print("Transpose of the matrix:")
            print(transpose_matrix(mat))

        elif choice == '5':  # Matrix Determinant
            print("Matrix (must be square):")
            mat = input_matrix()
            if mat.shape[0] == mat.shape[1]:
                print(f"Determinant of the matrix: {determinant_matrix(mat)}")
            else:
                print("Matrix must be square to calculate determinant.")

        elif choice == '6':  # Matrix Inverse
            print("Matrix (must be square):")
            mat = input_matrix()
            if mat.shape[0] == mat.shape[1]:
                inv = inverse_matrix(mat)
                if inv is not None:
                    print("Inverse of the matrix:")
                    print(inv)
                else:
                    print("Matrix is singular and does not have an inverse.")
            else:
                print("Matrix must be square to calculate inverse.")

        elif choice == '7':  # Matrix Adjoint
            print("Matrix (must be square):")
            mat = input_matrix()
            if mat.shape[0] == mat.shape[1]:
                adj = adjoint_matrix(mat)
                if adj is not None:
                    print("Adjoint of the matrix:")
                    print(adj)
            else:
                print("Matrix must be square to calculate adjoint.")

        elif choice == '8':  # Exit
            print("Exiting...")
            break

        elif choice == '0':
            print("CLOSING...")
            exit()

        else:
            print("Invalid choice! Please select from 1 to 8.")