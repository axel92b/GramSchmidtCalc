from src.logic import utility
import src.logic.regular_gram_schmidt as RGSC
import src.logic.custom_gram_schmidt as CGSC


def RegularGramSchmidt():
    while True:
        vectors = utility.get_matrix_from_user(5)
        if len(vectors) > 0:
            calc = RGSC.RegularGramSchmidt()
            result_matrix = calc.calc(vectors)
            if result_matrix is not None:
                print(result_matrix)
                utility.print_if_matrix_is_basis(result_matrix)
            answer = input("Start over? (Y/n)")
            if answer.lower() == 'n':
                break
            else:
                continue


def CustomGramSchmidt():
    while True:
        print("Enter the inner product matrix 3x3")
        inner_product_matrix = utility.get_matrix_from_user(3, True)
        calc = CGSC.CustomGramSchmidt(inner_product_matrix)
        print("Enter vectors from R(3)")
        vectors = utility.get_matrix_from_user(3)
        if len(vectors) > 0:
            result_matrix = calc.calc(vectors)
            if result_matrix is not None:
                print(result_matrix)
                utility.print_if_matrix_is_basis(result_matrix)
            answer = input("Start over? (Y/n)")
            if answer.lower() == 'n':
                break
            else:
                continue
