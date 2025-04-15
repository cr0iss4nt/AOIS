from truth_table import TruthTable


def build_perfect_conjunctive_normal_form(formula: str):
    truth_table = TruthTable(formula)
    formula = formula.replace(' ', '')
    answer_location = len(truth_table.columns) - 1
    answer = [i[answer_location] for i in truth_table.rows]
    conjunction = []
    for i, value in enumerate(answer):
        if value == '1':
            continue
        disjunction = []
        for j in range(len(truth_table.atoms)):
            letter = truth_table.columns[j]
            disjunction.append(f"!{letter}" if truth_table.rows[i][j] == '1' else f"{letter}")
        conjunction.append(f"({' | '.join(disjunction)})")
    return ' & '.join(conjunction)


def build_perfect_disjunctive_normal_form(formula: str):
    truth_table = TruthTable(formula)
    formula = formula.replace(' ', '')
    answer_location = len(truth_table.columns) - 1
    answer = [i[answer_location] for i in truth_table.rows]
    disjunction = []
    for i, value in enumerate(answer):
        if value == '0':
            continue
        conjunction = []
        for j in range(len(truth_table.atoms)):
            letter = truth_table.columns[j]
            conjunction.append(f"!{letter}" if truth_table.rows[i][j] == '0' else f"{letter}")
        disjunction.append(f"({' & '.join(conjunction)})")
    return ' | '.join(disjunction)
