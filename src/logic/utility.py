import numpy as np


def get_matrix_from_user(max_dimension: int, strict_dimension=False) -> np.ndarray:
    matrix = []
    print("Enter the vectors, each value separated by space and each vector separated by enter. "
          "Enter 'q' on new line to end the input")
    while len(matrix) < max_dimension:
        vector = input("Enter vector: ")
        if len(vector) == 0:
            continue

        if vector[0] == 'q' and not strict_dimension:
            break

        float_vector = [float(i) for i in vector.split(' ')]
        matrix.append(float_vector)
        if len(float_vector) != len(matrix[0]):
            raise Exception("Vectors should be the same size!")
    return np.array(matrix)


def print_if_matrix_is_basis(matrix: np.ndarray):
    if matrix.shape[0] == matrix.shape[1]:
        print(f"The result is basis for R({matrix.shape[1]})")
    else:
        print(f"The result is not basis for R({matrix.shape[1]})")
