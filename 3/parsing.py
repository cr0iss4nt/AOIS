def parse(form, subformulas):
    form = form.replace(" ", "")

    if form.isidentifier():
        subformulas.add(form)
        return form

    if form.startswith("!"):
        subformulas.add(form)
        sub_form = parse(form[1:], subformulas)
        return f"!{sub_form}"

    balance = 0
    main_operator = None
    for i, char in enumerate(form):
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        elif balance == 0 and char in "&|>~":
            main_operator = char
            break

    if main_operator:
        left = form[:i]
        right = form[i + 1:]
        subformulas.add(form)
        parse(left, subformulas)
        parse(right, subformulas)
        return f"({left} {main_operator} {right})"

    if form.startswith("(") and form.endswith(")"):
        inner_form = form[1:-1]
        subformulas.add(form)
        return parse(inner_form, subformulas)

    return form


def find_subformulas(formula):
    subformulas = set()

    parse(formula, subformulas)

    subformulas_list = list(subformulas)
    for i in subformulas_list:
        if f'({i})' in subformulas_list:
            subformulas_list.remove(f'({i})')

    return sorted(subformulas_list, key=lambda s: (len(s), s))
