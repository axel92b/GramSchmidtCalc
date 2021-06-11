import numpy as np
import numpy.linalg


def get_matrix() -> np.ndarray:
    return np.array([
        [0, 3, 4],
        [1, 0, 1],
        [1, 1, 3]
    ])


def projection(a: np.array, b: np.array) -> np.array:
    return (np.dot(a, b) / np.dot(b, b)) * b


def get_vec_normal(a: np.array) -> float:
    return np.dot(a, a) ** 0.5


def normalize_vec(a: np.array) -> np.array:
    vec_normal = get_vec_normal(a)
    for i, val in enumerate(a):
        a[i] = val / vec_normal


def gram_schmidt_calc(a: np.ndarray) -> np.ndarray:
    b: np.ndarray = a.copy()[:].astype(numpy.float32)
    for i in range(0, b.shape[0] - 1):
        for j in range(i + 1, b.shape[0]):
            b[j] -= projection(b[j], b[i])
        normalize_vec(b[i])
    normalize_vec(b[-1])
    return b


def main():
    matrix = get_matrix()
    if numpy.linalg.matrix_rank(matrix) != matrix.shape[0]:
        raise Exception("Linearly dependant vectors are inside")
    print(gram_schmidt_calc(matrix))


if __name__ == '__main__':
    main()
