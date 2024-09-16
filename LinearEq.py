import numpy as np
# Function to display the algorithm menu
def algorithm_menu():
    print("---------------------------- LINEAR EQUATIONS MENU -----------------------------------")
    print("Choose the algorithm to solve the system of linear equations:")
    print("1. Gaussian Elimination (with steps)")
    print("2. Inverse Matrix Method (X = A^(-1) * B)")
    print("3. Solve using NumPy")
    print("4. Exit (go back to main menu)")
    print("0. CLOSE THE PROGRAM")
    print("---------------------------------------------------------------")

# Function to input the system of equations as matrix A and B
def input_system():
    n = int(input("Enter the number of variables: "))
    print("Enter the coefficients matrix A (row-wise):")
    A = []
    for i in range(n):
        row = list(map(float, input().split()))
        A.append(row)
    A = np.array(A)

    print("Enter the constant matrix B:")
    B = []
    for i in range(n):
        b = float(input())
        B.append(b)
    B = np.array(B)

    return A, B
# Gaussian Elimination method
def gaussian_elimination(A, B):
    n = len(B)
    # Augment matrix A with matrix B
    augmented_matrix = np.column_stack((A, B))
    print("\nInitial Augmented Matrix:")
    print(augmented_matrix)

    # Forward Elimination
    for i in range(n):
        print(f"\n### Step {i+1} (Pivot row {i+1}):")

        pivot = augmented_matrix[i][i]
        print(f"Pivot element before normalization: {pivot}")

        if pivot == 0:
            print(f"Cannot find non-zero pivot in column {i+1}, skipping.")
            for j in range(i+1, n):
                if augmented_matrix[j][i] != 0:
                    print(f"Swapping row {i+1} with row {j+1} for non-zero pivot:")
                    augmented_matrix[[i, j]] = augmented_matrix[[j, i]]
                    break
        augmented_matrix[i] = augmented_matrix[i] / pivot
        for j in range(i+1, n):
            factor = augmented_matrix[j][i]
            augmented_matrix[j] = augmented_matrix[j] - factor * augmented_matrix[i]

        # print(f"step {i+1} (Forward Elimination):")
        print(f"Normalized pivot row {i+1}:")
        print(augmented_matrix)

    # Back Substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = augmented_matrix[i][-1] - np.sum(augmented_matrix[i][i+1:n] * x[i+1:n])
        print(f"Back Substitution for x[{i+1}] = {x[i]}")

    print("\nSolution Vector X:")
    print(x)
    return x

# Inverse Matrix Method
def inverse_matrix_method(A, B):
    try:
        A_inv = np.linalg.inv(A)
        print("\nInverse of matrix A:")
        print(A_inv)

        X = np.dot(A_inv, B)
        print("\nSolution Vector X = A^(-1) * B:")
        print(X)
        return X
    except np.linalg.LinAlgError:
        print("Matrix A is singular and cannot be inverted.")
        return None

# Solve using NumPy's built-in function
def numpy_solve(A, B):
    try:
        X = np.linalg.solve(A, B)
        print("\nSolution Vector X (using NumPy):")
        print(X)
        return X
    except np.linalg.LinAlgError:
        print("Matrix A is singular or the system has no unique solution.")
        return None

# Main function to run the program
def run_Linear_Equation ():
    while True:
        algorithm_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':  # Gaussian Elimination
            A, B = input_system()
            print("\nSolving using Gaussian Elimination:")
            gaussian_elimination(A, B)

        elif choice == '2':  # Inverse Matrix Method
            A, B = input_system()
            print("\nSolving using Inverse Matrix Method:")
            inverse_matrix_method(A, B)

        elif choice == '3':  # NumPy Solve (No steps)
            A, B = input_system()
            print("\nSolving using NumPy's built-in function:")
            numpy_solve(A, B)

        elif choice == '4':  # Exit
            print("Exiting...")
            break

        elif choice == '0':
            print("CLOSING...")
            exit()
            
        else:
            print("Invalid choice! Please select from 1 to 8.")
# Run the program
