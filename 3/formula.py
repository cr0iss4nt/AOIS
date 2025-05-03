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
    new_formula = formula
    old_formula = ""
    while new_formula != old_formula:
        old_formula = new_formula

        new_formula = new_formula.replace("!1", "0")
        new_formula = new_formula.replace("!0", "1")

        subformula_pattern = r"[01][&\|>~][01]"
        subformula_location = re.search(subformula_pattern, new_formula)
        if subformula_location:
            subformula = new_formula[subformula_location.start(): subformula_location.end()]
            new_formula = new_formula.replace(subformula, evaluate(subformula))

        new_formula = new_formula.replace("(1)", "1")
        new_formula = new_formula.replace("(0)", "0")
    return new_formula


def replace_by_pattern_singular_value(pattern, formula, value):
    location = re.search(pattern, formula)
    if location:
        subformula = formula[location.start(): location.end()]
        formula = formula.replace(subformula, value)
    return formula


def partially_evaluate_formula(formula):
    old_formula = ""
    new_formula = formula

    while new_formula != old_formula:
        old_formula = new_formula

        new_formula = new_formula.replace("!1", "0")
        new_formula = new_formula.replace("!0", "1")

        new_formula = replace_by_pattern_singular_value(r"1 \| ![A-Za-z]", new_formula, "1")
        new_formula = replace_by_pattern_singular_value(r"1 \| [A-Za-z]", new_formula, "1")

        new_formula = replace_by_pattern_singular_value(r"![A-Za-z] \| 1", new_formula, "1")
        new_formula = replace_by_pattern_singular_value(r"[A-Za-z] \| 1", new_formula, "1")

        new_formula = replace_by_pattern_singular_value(r"0 & ![A-Za-z]", new_formula, "0")
        new_formula = replace_by_pattern_singular_value(r"0 & [A-Za-z]", new_formula, "0")

        new_formula = replace_by_pattern_singular_value(r"![A-Za-z] & 0", new_formula, "0")
        new_formula = replace_by_pattern_singular_value(r"[A-Za-z] & 0", new_formula, "0")

        new_formula = new_formula.replace("1 & ", "")
        new_formula = new_formula.replace(" & 1", "")

        new_formula = new_formula.replace(r"0 \| ", "")
        new_formula = new_formula.replace(r" \| 0", "")

        new_formula = new_formula.replace("(1)", "1")
        new_formula = new_formula.replace("(0)", "0")

        new_formula = re.sub(r"\((.*?)\)\s*\|\s*0", r"(\1)", new_formula)
        new_formula = re.sub(r"\((.*?)\)\s*&\s*0", r"0", new_formula)
        new_formula = re.sub(r"\((.*?)\)\s*\|\s*1", r"1", new_formula)
        new_formula = re.sub(r"0\s*&\s*\((.*?)\)", r"0", new_formula)
        new_formula = re.sub(r"1\s*\|\s*\((.*?)\)", r"1", new_formula)

        new_formula = re.sub(r'\((!?[A-Za-z])\)', r'\1', new_formula)

        new_formula = new_formula.replace("0 & 0", "0")
        new_formula = new_formula.replace("1 | 1", "1")
        new_formula = new_formula.replace("0 | 1", "1")
        new_formula = new_formula.replace("1 | 0", "1")

    return new_formula
