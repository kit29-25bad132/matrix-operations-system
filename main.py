from operations import add_matrix, subtract_matrix, multiply_matrix, display_matrix


def input_matrix(rows, cols):
    matrix = []
    print("Enter matrix elements row by row:")
    
    for i in range(rows):
        while True:
            row = input(f"Row {i+1}: ").split()
            if len(row) != cols:
                print("Invalid input! Enter exactly", cols, "values.")
            else:
                matrix.append(list(map(int, row)))
                break
    return matrix


# Taking input
r1 = int(input("Enter rows of Matrix A: "))
c1 = int(input("Enter columns of Matrix A: "))
A = input_matrix(r1, c1)

r2 = int(input("\nEnter rows of Matrix B: "))
c2 = int(input("Enter columns of Matrix B: "))
B = input_matrix(r2, c2)


# Menu
while True:
    print("\n--- MENU ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Display Matrices")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        if r1 == r2 and c1 == c2:
            result = add_matrix(A, B)
            print("Addition Result:")
            display_matrix(result)
        else:
            print("Addition not possible!")

    elif choice == '2':
        if r1 == r2 and c1 == c2:
            result = subtract_matrix(A, B)
            print("Subtraction Result:")
            display_matrix(result)
        else:
            print("Subtraction not possible!")

    elif choice == '3':
        if c1 == r2:
            result = multiply_matrix(A, B)
            print("Multiplication Result:")
            display_matrix(result)
        else:
            print("Multiplication not possible!")

    elif choice == '4':
        print("\nMatrix A:")
        display_matrix(A)
        print("Matrix B:")
        display_matrix(B)

    elif choice == '5':
        print("Exited successfully!")
        break

    else:
        print("Invalid choice!")