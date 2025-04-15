import re

from formula_evaluation import evaluate


def normalize(formula):
    formula = formula.replace(' ', '')
    formula = re.sub(r'(!!)+', '', formula)
    formula = re.sub(r'!(\w)', r'(!\1)', formula)
    while formula.startswith('(') and formula.endswith(')'):
        balance = 0
        for i, char in enumerate(formula):
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
            if balance == 0:
                break
        if balance == 0 and i == len(formula) - 1:
            formula = formula[1:-1].strip()
        else:
            break
    return formula


def is_atomic_formula(formula):
    pattern = "^([A-Za-z])$"
    return bool(re.match(pattern, formula))


def evaluate_formula(formula):
    while formula not in ['1', '0']:
        formula = formula.replace("!1", "0")
        formula = formula.replace("!0", "1")

        subformula_pattern = r"[01][&\|>~][01]"
        subformula_location = re.search(subformula_pattern, formula)
        if subformula_location:
            subformula = formula[subformula_location.start(): subformula_location.start() + 3]
            formula = formula.replace(subformula, evaluate(subformula))

        formula = formula.replace("(1)", "1")
        formula = formula.replace("(0)", "0")
    return formula
