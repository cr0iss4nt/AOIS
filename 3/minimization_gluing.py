from itertools import combinations

from prettytable import PrettyTable

from formula import partially_evaluate_formula


def term_to_bits(term, variables):
    bits = []
    for var in variables:
        if f"!{var}" in term:
            bits.append('0')
        elif var in term:
            bits.append('1')
        else:
            raise ValueError
    return ''.join(bits)


def bits_to_term(bits, variables, is_conjunction):
    term = []
    for var, bit in zip(variables, bits):
        if bit == '1':
            term.append(var)
        elif bit == '0':
            term.append(f"!{var}")
        else:
            pass
    return f"({(' & ' if not is_conjunction else ' | ').join(term)})"


def find_implicants(terms):
    implicants = set()
    used = set()
    for t1, t2 in combinations(terms, 2):
        diff = sum(1 for a, b in zip(t1, t2) if a != b)
        if diff == 1:
            new_term = ''.join(a if a == b else '-' for a, b in zip(t1, t2))
            implicants.add(new_term)
            used.add(t1)
            used.add(t2)
    for term in terms:
        if term not in used:
            implicants.add(term)
    return implicants


def implicant_covered(imp_bits, term_bits):
    for imp_bit, term_bit in zip(imp_bits, term_bits):
        if imp_bit != '-' and imp_bit != term_bit:
            return False
    return True


def gluing(variables, terms, is_conjunction):
    current_terms = {term_to_bits(term, variables) for term in terms}
    prev_terms = set()

    while current_terms != prev_terms:
        prev_terms = current_terms
        current_terms = find_implicants(current_terms)

    if not is_conjunction:
        print("Фаза склейки:",
              ' | '.join([bits_to_term(term, variables, is_conjunction=False) for term in current_terms]))
    else:
        print("Фаза склейки:",
              ' & '.join([bits_to_term(term, variables, is_conjunction=True) for term in current_terms]))
    return list(current_terms)


def minimize_implicant_check(form: str, is_conjunction):
    if form == "не существует":
        return "не существует"

    variables = sorted(list(set([i for i in form if i.isalpha()])))
    pnf_terms = form.split(' | ' if not is_conjunction else ' & ')

    current_terms = gluing(variables, pnf_terms, is_conjunction)

    for term in list(current_terms):
        substituted_terms = current_terms.copy()
        substituted_terms.remove(term)
        substituted_form = (' | ' if not is_conjunction else ' & ').join(
            bits_to_term(i, variables, is_conjunction) for i in substituted_terms)

        for i in range(len(term)):
            if term[i] != '-':
                substituted_form = substituted_form.replace(variables[i], term[i])
        partial_evaluation = partially_evaluate_formula(substituted_form)
        removal_bit = str(int(not is_conjunction))
        if partial_evaluation == removal_bit:
            current_terms.remove(term)

    minimized_terms = [bits_to_term(term, variables, is_conjunction) for term in current_terms]
    return (' | ' if not is_conjunction else ' & ').join(minimized_terms)


def minimize_chart(form: str, is_conjunction):
    if form == "не существует":
        return "не существует"

    variables = sorted(list(set([i for i in form if i.isalpha()])))
    terms = form.split(' | ' if not is_conjunction else ' & ')

    original_bits = [term_to_bits(term, variables) for term in terms]
    current_bits = gluing(variables, terms, is_conjunction)
    current_terms = [bits_to_term(bits, variables, is_conjunction) for bits in current_bits]

    coverage = []
    for imp in current_bits:
        row = []
        for term in original_bits:
            row.append(implicant_covered(imp, term))
        coverage.append(row)

    output_chart(terms, current_terms, coverage)

    essential = set()
    for j in range(len(original_bits)):
        covering_imps = [i for i in range(len(current_bits)) if coverage[i][j]]
        if len(covering_imps) == 1:
            essential.add(covering_imps[0])

    non_redundant = []
    for i in range(len(current_bits)):
        if i in essential:
            non_redundant.append(current_terms[i])
            continue

        is_redundant = True
        for j in range(len(original_bits)):
            if coverage[i][j]:
                other_imps_cover = any(
                    coverage[k][j] for k in range(len(current_bits))
                    if k != i
                )
                if not other_imps_cover:
                    is_redundant = False
                    break

        if not is_redundant:
            non_redundant.append(current_terms[i])

    return (' | ' if not is_conjunction else ' & ').join(non_redundant)


def output_chart(original, glued, coverage):
    chart = PrettyTable([''] + original)
    for i in range(len(coverage)):
        row = [glued[i]] + ['x' if coverage[i][j] else '' for j in range(len(coverage[i]))]
        chart.add_row(row)
    print("Таблица:")
    print(chart)
