from prettytable import PrettyTable

from formula import is_atomic_formula, evaluate_formula
from parsing import find_subformulas


class TruthTable:
    def __init__(self, formula: str):
        subformulas = find_subformulas(formula)
        self.atoms = [i for i in subformulas if is_atomic_formula(i)]
        self.columns = subformulas
        self.rows = [['0'] * len(self.columns) for _ in range(2 ** len(self.atoms))]
        self.length = len(self.rows)
        self.width = len(self.columns)
        self.fill_atoms()
        self.fill_table()

    def fill_atoms(self):
        num_rows = 2 ** len(self.atoms)
        for i in range(num_rows):
            self.rows[i][:len(self.atoms)] = format(i, f"0{len(self.atoms)}b")

    def fill_cell(self, letters, row, column, formula):
        for k in letters:
            horizontal_location = self.columns.index(k)
            table_value = self.rows[row][horizontal_location]
            formula = formula.replace(k, table_value)
        self.rows[row][column] = evaluate_formula(formula)
        return self.rows[row][column]

    def fill_table(self):
        for i in range(self.length):
            for j in range(len(self.atoms), self.width):
                form = self.columns[j]
                letters = [s for s in form if s.isalpha()]
                self.rows[i][j] = self.fill_cell(letters, i, j, form)

    def output(self):
        pretty_table = PrettyTable(self.columns)
        pretty_table.add_rows(self.rows)
        print(pretty_table)
