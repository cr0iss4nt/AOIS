import random

from matrix_const import SIZE, V_LENGTH, A_LENGTH, B_LENGTH
from matrix_functions import summarize_binary



class Matrix:
    def __init__(self):
        self.matrix = [[str(random.randint(0, 1)) for _ in range(SIZE)] for _ in range(SIZE)]

    def output(self):
        for row in self.matrix:
            for i in row:
                print(i,end=' ')
            print()

    def get_word(self, index):
        if not 0 <= index < SIZE:
            raise ValueError
        word = ""
        for i in range(SIZE):
            row = (i + index) % SIZE
            word += self.matrix[row][index]
        return word

    def replace_word(self, index, word):
        if not 0 <= index < SIZE:
            raise ValueError
        if not all(i in ['0','1'] for i in word):
            raise ValueError
        if len(word) != SIZE:
            raise ValueError

        for i in range(SIZE):
            row = (i + index) % SIZE
            self.matrix[row][index] = word[i]

    def get_diagonal(self, index):
        if not 0 <= index < SIZE:
            raise ValueError

        diagonal = ""
        i = index
        for j in range(SIZE):
            diagonal += self.matrix[i][j]
            i = (i+1) % SIZE
        return diagonal

    def replace_diagonal(self, index, diagonal):
        if not 0 <= index < SIZE:
            raise ValueError
        if not all(i in ['0','1'] for i in diagonal):
            raise ValueError
        if len(diagonal) != SIZE:
            raise ValueError

        i = index
        for j in range(SIZE):
            self.matrix[i][j] = diagonal[j]
            i = (i+1) % SIZE

    def logic(self, diagonal1_number:int, diagonal2_number:int, result_diagonal_number:int, function_number:str):
        if function_number not in ["0", "5", "10", "15"]:
            raise ValueError
        if not 0 <= diagonal1_number < SIZE:
            raise ValueError
        if not 0 <= diagonal2_number < SIZE:
            raise ValueError
        if not 0 <= result_diagonal_number < SIZE:
            raise ValueError

        diagonal2 = self.get_diagonal(diagonal2_number)
        result = ""
        for i in range(SIZE):
            match function_number:
                case '0':
                    result += '0'
                case '15':
                    result += '1'
                case '5':
                    result += diagonal2[i]
                case '10':
                    result += '0' if diagonal2[i] == '1' else '1'
        self.replace_diagonal(result_diagonal_number, result)

    def summarize_words(self, given_V):
        if not all(i in ['0','1'] for i in given_V):
            raise ValueError
        if len(given_V) != 3:
            raise ValueError


        for i in range(SIZE):
            word = self.get_word(i)
            V = word[:V_LENGTH]
            if V == given_V:
                A_end = V_LENGTH+A_LENGTH
                B_end = A_end + B_LENGTH
                A = word[V_LENGTH:A_end]
                B = word[A_end:B_end]
                S = summarize_binary(A, B).zfill(5)
                new_word = V+A+B+S
                self.replace_word(i, new_word)

    def search_by_match(self, argument:str):
        if not all(i in ['0','1'] for i in argument):
            raise ValueError
        if not 0 < len(argument) <= SIZE:
            raise ValueError

        argument = argument.zfill(SIZE)
        max_matches = 0
        best_candidate_index = -1
        for j in range(SIZE):
            word = self.get_word(j)
            matches = sum(1 for i in range(SIZE) if word[i] == argument[i])
            if matches > max_matches:
                max_matches = matches
                best_candidate_index = j
        return best_candidate_index, max_matches



