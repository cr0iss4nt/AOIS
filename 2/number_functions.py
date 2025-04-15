from truth_table import TruthTable


def index_form(formula: str):
    truth_table = TruthTable(formula)
    formula = formula.replace(' ', '')
    answer_location = truth_table.columns.index(formula)
    answer = [i[answer_location] for i in truth_table.rows]
    number = int(''.join(answer), 2)
    return number


def number_perfect_conjunctive_normal_form(formula: str):
    truth_table = TruthTable(formula)
    formula = formula.replace(' ', '')
    answer_location = truth_table.columns.index(formula)
    answer = [i[answer_location] for i in truth_table.rows]
    numbers = []
    for i, value in enumerate(answer):
        if value == '0':
            numbers.append(i)
    return numbers


def number_perfect_disjunctive_normal_form(formula: str):
    truth_table = TruthTable(formula)
    formula = formula.replace(' ', '')
    answer_location = truth_table.columns.index(formula)
    answer = [i[answer_location] for i in truth_table.rows]
    numbers = []
    for i, value in enumerate(answer):
        if value == '1':
            numbers.append(i)
    return numbers
