list_conjunction = [(0, 0), (0, 1), (1, 0)], [(1, 1)]
list_disjunction = [(0, 0)], [(0, 1), (1, 0), (1, 1)]
list_implication = [(1, 0)], [(0, 0), (0, 1), (1, 1)]
list_equivalence = [(1, 0), (0, 1)], [(0, 0), (1, 1)]


def evaluate(subformula):
    value1, value2 = subformula[0], subformula[2]
    sign = subformula[1]
    pair = (int(value1), int(value2))
    match sign:
        case '&':
            zero_list, one_list = list_conjunction
        case '|':
            zero_list, one_list = list_disjunction
        case '>':
            zero_list, one_list = list_implication
        case '~':
            zero_list, one_list = list_equivalence

    if pair in one_list:
        return '1'
    if pair in zero_list:
        return '0'
    return ValueError
