def normalize_term_name(term):
    return term[0].upper() + term[1:].lower()


def table_term(table, term):
    return f"{term} - {table.get(term)}."
