from prettytable import PrettyTable

from minimization_gluing import term_to_bits


def gray_list(n):
    result = []
    for i in range(1 << n):
        gray_num_decimal = i ^ (i >> 1)
        gray_num_binary = []
        while gray_num_decimal > 0:
            gray_num_binary.append(str(gray_num_decimal % 2))
            gray_num_decimal //= 2
        result.append(''.join(gray_num_binary)[::-1].zfill(n))
    return result


def create_karnaugh_map(formula, is_conjunction: bool = False):
    variables = sorted(list(set([i for i in formula if i.isalpha()])))

    if not is_conjunction:
        formula_terms = formula.split(' | ')
        terms_bits = [term_to_bits(term, variables) for term in formula_terms]
    else:
        formula_terms = formula.split(' & ')
        terms_bits = [term_to_bits(term, variables) for term in formula_terms]
        terms_bits = [''.join('1' if j == '0' else '0' for j in i) for i in terms_bits]

    length = len(variables)

    gray_1 = gray_list(length // 2)
    gray_2 = gray_list(length - length // 2)
    rows = [i for i in gray_1]
    columns = [i for i in gray_2]

    karnaugh_map = []
    for row in rows:
        true_bit = str(int(not is_conjunction))
        false_bit = str(int(is_conjunction))
        karnaugh_map.append([true_bit if row + column in terms_bits else false_bit for column in columns])

    return columns, rows, karnaugh_map


def create_karnaugh_map_for_five(formula, is_conjunction: bool = False):
    variables = sorted(list(set([i for i in formula if i.isalpha()])))

    if not is_conjunction:
        formula_terms = formula.split(' | ')
        terms_bits = [term_to_bits(term, variables) for term in formula_terms]
    else:
        formula_terms = formula.split(' & ')
        terms_bits = [term_to_bits(term, variables) for term in formula_terms]
        terms_bits = [''.join('1' if j == '0' else '0' for j in i) for i in terms_bits]
    terms_bits_0 = [i[1:] for i in terms_bits if i[0] == '0']
    terms_bits_1 = [i[1:] for i in terms_bits if i[0] == '1']

    length = 4

    gray_1 = gray_list(length // 2)
    gray_2 = gray_list(length - length // 2)
    rows = [i for i in gray_1]
    columns = [i for i in gray_2]

    karnaugh_map_0 = []
    karnaugh_map_1 = []
    for row in rows:
        true_bit = str(int(not is_conjunction))
        false_bit = str(int(is_conjunction))
        karnaugh_map_0.append([true_bit if row + column in terms_bits_0 else false_bit for column in columns])
        karnaugh_map_1.append([true_bit if row + column in terms_bits_1 else false_bit for column in columns])

    return columns, rows, karnaugh_map_0, karnaugh_map_1


def output_karnaugh_map(columns, rows, karnaugh_map):
    table = PrettyTable([''] + columns)
    for i, row in enumerate(rows):
        table.add_row([row] + karnaugh_map[i])

    print(table)


def find_rectangles(karnaugh_map, is_conjunction: bool):
    row_length = len(karnaugh_map)
    column_length = len(karnaugh_map[0]) if row_length > 0 else 0
    rectangles = []

    power_of_two_lengths = get_power_of_two_lengths(max(row_length, column_length))

    for x1 in range(row_length):
        for y1 in range(column_length):
            find_rectangles_from_point(karnaugh_map, x1, y1, rectangles, power_of_two_lengths, row_length,
                                       column_length, is_conjunction=is_conjunction)

    return list(set(rectangles))


def get_power_of_two_lengths(max_length):
    return [i for i in range(1, max_length + 1) if (i & (i - 1)) == 0]


def find_rectangles_from_point(karnaugh_map, x1, y1, rectangles, power_of_two_lengths, row_length, column_length,
                               is_conjunction: bool):
    for length in power_of_two_lengths:
        for width in power_of_two_lengths:
            x2 = x1 + length - 1
            y2 = y1 + width - 1

            if is_rectangle(karnaugh_map, x1, y1, x2, y2, row_length, column_length, is_conjunction=is_conjunction):
                rectangles.append(((x1, y1), (x2 % row_length, y2 % column_length)))


def is_rectangle(karnaugh_map, x1, y1, x2, y2, row_length, column_length, is_conjunction: bool):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            wrapped_i = i % row_length
            wrapped_j = j % column_length
            if karnaugh_map[wrapped_i][wrapped_j] == str(int(is_conjunction)):
                return False
    return True


def rectangle_to_term(rectangle, variables, rows, columns, is_conjunction: bool):
    (x1, y1), (x2, y2) = rectangle
    row_len = len(rows)
    col_len = len(columns)
    if x1 > x2:
        x2 += row_len
    if y1 > y2:
        y2 += col_len
    addresses = []

    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            row_bits = rows[i % len(rows)]
            col_bits = columns[j % len(columns)]
            addresses.append(row_bits + col_bits)

    common_bits = list(addresses[0])
    for bits in addresses[1:]:
        for idx in range(len(bits)):
            if common_bits[idx] != bits[idx]:
                common_bits[idx] = 'x'

    term = []
    for idx, bit in enumerate(common_bits):
        true_bit = str(int(not is_conjunction))
        false_bit = str(int(is_conjunction))
        if bit == true_bit:
            term.append(variables[idx])
        elif bit == false_bit:
            term.append(f"!{variables[idx]}")

    if not is_conjunction:
        return f"({' & '.join(term)})" if term else '1'
    else:
        return f"({' | '.join(term)})" if term else '0'


def is_rectangle_ones_in_both_maps(karnaugh_map_0, karnaugh_map_1, rectangle, is_conjunction):
    row_len = len(karnaugh_map_0)
    col_len = len(karnaugh_map_0[0])
    (x1, y1), (x2, y2) = rectangle
    if x1 > x2:
        x2 += row_len
    if y1 > y2:
        y2 += col_len

    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            xi, yj = i % row_len, j % col_len
            if karnaugh_map_0[xi][yj] != str(int(not is_conjunction)) \
                    or karnaugh_map_1[xi][yj] != str(int(not is_conjunction)):
                return False
    return True


def minimize_karnaugh(form, is_conjunction):
    if form == "не существует":
        return "не существует"

    variables = set([i for i in form if i.isalpha()])
    if len(variables) > 5:
        raise ValueError("Слишком много переменных")
    elif len(variables) == 5:
        columns, rows, karnaugh_map_0, karnaugh_map_1 =(
            create_karnaugh_map_for_five(form, is_conjunction=is_conjunction))
        output_karnaugh_map(columns, rows, karnaugh_map_0)
        output_karnaugh_map(columns, rows, karnaugh_map_1)

        rectangles0 = find_rectangles(karnaugh_map_0, is_conjunction=is_conjunction)
        rectangles1 = find_rectangles(karnaugh_map_1, is_conjunction=is_conjunction)

        rectangles0 = sorted(rectangles0, key=lambda rect: -rectangle_area(rect, len(rows), len(columns)))
        rectangles1 = sorted(rectangles1, key=lambda rect: -rectangle_area(rect, len(rows), len(columns)))

        variables = sorted(list(set([i for i in form if i.isalpha()])))
        covered0 = set()
        covered1 = set()
        final_terms = []

        for rectangle_0 in rectangles0:
            points0 = rectangle_points(rectangle_0, len(rows), len(columns))
            if points0.issubset(covered0):
                continue
            for rectangle_1 in rectangles1:
                points1 = rectangle_points(rectangle_1, len(rows), len(columns))
                if points0 == points1 and not points1.issubset(covered1) \
                        and is_rectangle_ones_in_both_maps(karnaugh_map_0, karnaugh_map_1, rectangle_0, is_conjunction):
                    term = rectangle_to_term(rectangle_0, variables[1:], rows, columns, is_conjunction)
                    final_terms.append(term)
                    covered0.update(points0)
                    covered1.update(points1)
                    break
            else:
                term = rectangle_to_term(rectangle_0, variables[1:], rows, columns, is_conjunction)
                if not is_conjunction:
                    final_terms.append(f"(!{variables[0]} & {term[1:-1]})")
                else:
                    final_terms.append(f"({variables[0]} | {term[1:-1]})")
                covered0.update(points0)

        for rectangle_1 in rectangles1:
            points1 = rectangle_points(rectangle_1, len(rows), len(columns))
            if points1.issubset(covered1):
                continue
            term = rectangle_to_term(rectangle_1, variables[1:], rows, columns, is_conjunction)
            if not is_conjunction:
                final_terms.append(f"({variables[0]} & {term[1:-1]})")
            else:
                final_terms.append(f"(!{variables[0]} | {term[1:-1]})")
            covered1.update(points1)

        if not is_conjunction:
            return ' | '.join(final_terms)
        else:
            return ' & '.join(final_terms)

    else:
        columns, rows, kmap = create_karnaugh_map(form, is_conjunction=is_conjunction)
        output_karnaugh_map(columns, rows, kmap)
        rectangles = find_rectangles(kmap, is_conjunction=is_conjunction)

        rectangles = sorted(rectangles, key=lambda rect: -rectangle_area(rect, len(rows), len(columns)))

        variables = sorted(list(set([i for i in form if i.isalpha()])))
        covered = set()
        final_terms = []

        for rectangle in rectangles:
            points = rectangle_points(rectangle, len(rows), len(columns))
            if not points.issubset(covered):
                final_terms.append(rectangle_to_term(rectangle, variables, rows, columns, is_conjunction))
                covered.update(points)

        if not is_conjunction:
            return ' | '.join(final_terms)
        else:
            return ' & '.join(final_terms)


def rectangle_points(rectangle, row_len, col_len):
    (x1, y1), (x2, y2) = rectangle
    if x1 > x2:
        x2 += row_len
    if y1 > y2:
        y2 += col_len
    points = set()
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            points.add((i % row_len, j % col_len))
    return points


def rectangle_area(rectangle, row_len, col_len):
    (x1, y1), (x2, y2) = rectangle
    width = (x2 - x1 + 1) if x2 >= x1 else (row_len - x1 + x2 + 1)
    height = (y2 - y1 + 1) if y2 >= y1 else (col_len - y1 + y2 + 1)
    return width * height
