import numpy as np
import numpy.linalg


class CustomGramSchmidt:
    inner_product_matrix: np.ndarray

    def __init__(self, inner_product_matrix: np.ndarray) -> None:
        if self.__check__if_matrix_is_absolutely_positive(inner_product_matrix) == False:
            raise Exception("The provided matrix is not absolutely positive!")
        self.inner_product_matrix = inner_product_matrix

    def inner_product(self, a: np.array, b: np.array):
        return np.matmul(np.matmul(a, self.inner_product_matrix), b)

    def __projection(self, a: np.array, b: np.array) -> np.array:

        return (self.inner_product(a, b) / self.inner_product(b, b)) * b

    def __get_vec_normal(self, a: np.array) -> float:
        return self.inner_product(a, a) ** 0.5

    def __normalize_vec(self, a: np.array) -> np.array:
        vec_normal = self.__get_vec_normal(a)
        for i, val in enumerate(a):
            a[i] = val / vec_normal

    def calc(self, matrix: np.ndarray) -> np.ndarray:
        if self.is_matrix_linearly_dependent(matrix):
            raise Exception("Error: Matrix is linearly dependent")
        res: np.ndarray = matrix.copy()[:].astype(numpy.float32)
        for i in range(0, res.shape[0] - 1):
            for j in range(i + 1, res.shape[0]):
                res[j] -= self.__projection(res[j], res[i])
            self.__normalize_vec(res[i])
        self.__normalize_vec(res[-1])
        return res

    @staticmethod
    def is_matrix_linearly_dependent(a):
        return numpy.linalg.matrix_rank(a) != a.shape[0]

    @staticmethod
    def __check__if_matrix_is_absolutely_positive(inner_product_matrix):
        return np.all(np.linalg.eigvals(inner_product_matrix) > 0)




def main():
    matrix = np.array([[0, 3, 4],
                       [1, 0, 1],
                       [1, 1, 3]])
    gsc = CustomGramSchmidt(np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]]))
    result = gsc.calc(matrix)
    if not CustomGramSchmidt.is_matrix_linearly_dependent(result):
        print("The result is an ortonormal basis for the field")
    print(result)


if __name__ == '__main__':
    main()
