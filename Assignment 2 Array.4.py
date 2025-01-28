import numpy as np

A = np.array([[1, 2, 3],
              [0, 1, 4],
              [5, 6, 0]])

try:
    A_inv = np.linalg.inv(A)


    identity1 = np.dot(A, A_inv)
    identity2 = np.dot(A_inv, A)

    print("Matrix A:")
    print(A)

    print("\nInverse of A:")
    print(A_inv)

    print("\nA * A_inv:")
    print(identity1)

    print("\nA_inv * A:")
    print(identity2)

    print("\nIs A * A_inv close to the identity matrix?")
    print(np.allclose(identity1, np.eye(3)))

    print("\nIs A_inv * A close to the identity matrix?")
    print(np.allclose(identity2, np.eye(3)))

except np.linalg.LinAlgError:

    print("Matrix A is not invertible. Cannot compute its inverse.")