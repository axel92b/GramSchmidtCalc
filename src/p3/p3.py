import numpy as np
import numpy.linalg
from src.p1.p1 import GramSchmidtCalc as GSC
from src.p2.p2 import GramSchmidtCalc as GSC2

def a(x):
    return x ** 2 - 5 * x + 6


def b(x):
    return x ** 2 - 5 * x + 4

def main():
    matrix = np.array([[1, 2, 2, 0],
                       [0, -1, -1, 0],
                       [0, 0, 0, 3],
                       ])
    print(GSC().calc(matrix))
    """ q1 answer
        [[ 0.33333334  0.6666667   0.6666667   0.        ]
         [ 0.94280905 -0.23570225 -0.23570225  0.        ]
         [ 0.          0.          0.          1.        ]
        ]
    """
    """ q2 answer 
        1 = cf
        2 = 16ad+8ae+4af+8bd+4be+2bf+4cd+2ce+cf
        3 = ad+be-bf-bd+be-bf+cd-ce+cf
        res = 3cf + 17ad + 8ae +4af + 7bd + 6be  + 5cd + ce
    """
    g = GSC2(np.array([
        [17, 7, 5],
        [8, 6, 1],
        [4, 0, 3]
    ]))
    print(a(0)*b(0)+a(-1)*b(-1)+a(2)*b(2)+44)
    print(g.inner_product(np.array([1, -5, 6]), np.array([1, -5, 4])))

    print()


if __name__ == '__main__':
    main()
