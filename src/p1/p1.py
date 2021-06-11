import numpy as np
import numpy.linalg

class GramSchmidtCalc:

    def __projection(self, a: np.array, b: np.array) -> np.array:
        return (np.dot(a, b) / np.dot(b, b)) * b

    def __get_vec_normal(self, a: np.array) -> float:
        return np.dot(a, a) ** 0.5

    def __normalize_vec(self, a: np.array) -> np.array:
        vec_normal = self.__get_vec_normal(a)
        for i, val in enumerate(a):
            a[i] = val / vec_normal

    def calc(self, a: np.ndarray) -> np.ndarray:
        if numpy.linalg.matrix_rank(a) != a.shape[0]:
            raise Exception("Linearly dependant vectors are inside")
        b: np.ndarray = a.copy()[:].astype(numpy.float32)
        for i in range(0, b.shape[0] - 1):
            for j in range(i + 1, b.shape[0]):
                b[j] -= self.__projection(b[j], b[i])
            self.__normalize_vec(b[i])
        self.__normalize_vec(b[-1])
        return b


def main():
    matrix = np.array([[0,3,4],
                       [1,0,1],
                       [1,1,3]])
    gsc = GramSchmidtCalc()
    print(gsc.calc(matrix))


if __name__ == '__main__':
    main()
